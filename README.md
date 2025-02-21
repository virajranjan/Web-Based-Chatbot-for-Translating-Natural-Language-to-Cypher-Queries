# Web-Based-Chatbot-for-Translating-Natural-Language-to-Cypher-Queries
# Natural Language to Cypher Query Chatbot

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation Guide](#installation-guide)
- [Usage Instruction](#usage-instructions)
- [License](#license)

<a name="overview"></a>
## 1. Overview
This web-based chatbot translates natural language questions into Cypher queries for Neo4j databases. The system combines:

- **Hugging Face LLM**: For natural language understanding
- **Neo4j Database**: For graph data storage and querying
- **Flask Backend**: For API services
- **React Frontend**: For user interaction


<a name="features"></a>
## 2. Features
- Natural language to Cypher query conversion
- Real-time query execution
- Results visualization

<a name="installation-guide"></a>
## 3. Installation Guide
### Prerequisites
- Python 3.9+
- Node.js 16+
- Neo4j Desktop 4.4+

### Step-by-Step Setup

1. **Clone Repository**
   ```bash
    git clone git@github.com:virajranjan/Web-Based-Chatbot-for-Translating-Natural-Language-to-Cypher-Queries.git
    cd Web-Based-Chatbot-for-Translating-Natural-Language-to-Cypher-Queries 
   
2. **install python dependencies** 
   ```bash 
   cd backend
   pip install -r requirements.txt
3. **set Up Neo4j**
   Install, start a new database, and configure with username neo4j and password password.

4. **Install Frontend Dependencies**
   ```bash
   cd frontend
   npm install

<a name="usage-instructions"></a>
## 4. Usage Instruction
### Usage Instructions

1. **Start the backend**
   ```bash
   python app.py

2. **start the Frontend**
   ```bash
   cd frontend
   npm start
3. Open your browser and navigate to [http://localhost:3000](http://localhost:5000).

<a name="license"></a>
## 8. License

This project is licensed under the MIT License, with additional terms for dependencies:

- **Code**: MIT License 
- **Neo4j**: [Community License](https://neo4j.com/licensing/)



