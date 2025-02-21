import { useState } from "react";
import './App.css';
function App() {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setResponse(null);

    try {
      const res = await fetch("/api/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
      });

      const data = await res.json();

      if (res.ok) {
        setResponse(data);
      } else {
        setError(data.error);
      }
    } catch (err) {
      setError("Failed to connect to server");
    }
  };

  return (
    <div className="container">
      <div className="content">
        <h1>Text2Cypher</h1>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            placeholder="Ask a question..."
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
          />
          <button type="submit">Generate</button>
        </form>

        {response && (
          <div>
            <h2>Generated Cypher Query:</h2>
            <pre>{response.cypher}</pre>
            <h2>Query Results:</h2>
            <pre>{JSON.stringify(response.results, null, 2)}</pre>
          </div>
        )}

        {error && <p style={{ color: "red" }}>{error}</p>}
      </div>
    </div>
  );
}

export default App;
