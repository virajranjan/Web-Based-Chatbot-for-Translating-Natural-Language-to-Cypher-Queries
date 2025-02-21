import { useState } from 'react';
import './App.css';

function App() {
  const [question, setQuestion] = useState('');
  const [response, setResponse] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setResponse(null);
    setLoading(true);

    try {
      const res = await fetch('http://localhost:5000/api/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question }),
      });

      const data = await res.json();
      
      if (!res.ok) {
        throw new Error(data.error || 'Failed to generate query');
      }

      setResponse(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <header className="app-header">
        <h1>Text2Cypher</h1>
        <p>Natural Language to Neo4j Cypher Query Converter</p>
      </header>

      <main className="main-content">
        <form onSubmit={handleSubmit} className="query-form">
          <div className="input-group">
            <input
              type="text"
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              placeholder="Ask about your Neo4j data..."
              disabled={loading}
            />
            <button type="submit" disabled={loading}>
              {loading ? 'Generating...' : 'Generate Cypher'}
            </button>
          </div>
        </form>

        {error && <div className="error-message">{error}</div>}

        {response && (
          <div className="results-container">
            <div className="cypher-section">
              <h2>Generated Cypher Query</h2>
              <pre className="cypher-code">{response.cypher}</pre>
            </div>

            <div className="results-section">
              <h2>Query Results</h2>
              {response.results?.length > 0 ? (
                <pre className="results-data">
                  {JSON.stringify(response.results, null, 2)}
                </pre>
              ) : (
                <p className="no-results">No results found</p>
              )}
            </div>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;