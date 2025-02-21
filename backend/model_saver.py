import os
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from dotenv import load_dotenv
load_dotenv()
Token = os.getenv("HUGGING_FACE_TOKEN ")
save_path = "./saved_model"
model_name = "vprashant/cypher-gen"

def save_model(model_name, save_path):
    try:
        os.makedirs(save_path, exist_ok=True)

        config_path = os.path.join(save_path, "config.json")

        if os.path.exists(config_path):
            print(f"Model '{model_name}' exists at {save_path}. Skipping download.")
            return
        else:
            print(f"Downloading and saving '{model_name}' to {save_path}...")

        model = AutoModelForSeq2SeqLM.from_pretrained(model_name, token =Token)
        tokenizer = AutoTokenizer.from_pretrained(model_name,token =Token)

        # Save model and tokenizer
        print("Saving model and tokenizer...")
        model.save_pretrained(save_path)
        tokenizer.save_pretrained(save_path)

        print("Model and tokenizer saved successfully.")

    except Exception as e:
        print(f"Error: {str(e)}")
        
        if os.path.exists(save_path):
            print(f"Cleaning up partially downloaded files at {save_path}...")
            for filename in os.listdir(save_path):
                file_path = os.path.join(save_path, filename)
                os.remove(file_path)
            os.rmdir(save_path)

