from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from model_saver import save_model
import os 
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import logging
from neo4j import GraphDatabase 
from dotenv import load_dotenv

load_dotenv()

# Neo4j credentials
URI = os.getenv("NEO4J_URI")
AUTH = (os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))
DATABASE = os.getenv("NEO4J_DATABASE", "neo4j")  # Default to 'neo4j' if not set

model_path = "./saved_model"
model_name = "vprashant/cypher-gen"
save_model(model_name, model_path)

app = Flask(__name__)
CORS(app)

driver = GraphDatabase.driver(URI, auth=AUTH)

def run_query(cypher_query):
    """Runs a query on the specified Neo4j database."""
    try:
        with driver.session(database=DATABASE) as session:
            result = session.run(cypher_query)
            return [record.data() for record in result]
    except Exception as e:
        logging.exception(f"Error running query: {e}")
        raise

def generate_output(input_text, max_length=100):
    """Generates a Cypher query using the fine-tuned model."""
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

        # Tokenize input text
        input_ids = tokenizer(input_text, return_tensors="pt").input_ids

        # Generate output
        output_ids = model.generate(input_ids, max_length=max_length)
        output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

        return output_text
    except Exception as e:
        logging.exception(f"Error generating Cypher query: {e}")
        raise

@app.route('/api/generate', methods=['POST'])
def handle_query():
    """Handles the API request to generate and run a Cypher query."""
    try:
        data = request.json
        question = data.get('question', '')

        cypher_query = generate_output(question)

        results = run_query(cypher_query)

        return jsonify({
            "cypher": cypher_query,
            "result": results,
            "error": None
        })
    except Exception as e:
        return jsonify({
            "cypher": None,
            "result": None,
            "error": str(e)
        }), 500

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_frontend(path):
    """Serves the frontend from the 'frontend/build' directory."""
    if path and os.path.exists(f"frontend/build/{path}"):
        return send_from_directory('frontend/build', path)
    return send_from_directory('frontend/build', 'index.html')

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    finally:
        driver.close()  