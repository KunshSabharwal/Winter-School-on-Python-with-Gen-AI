## Forked from @https://github.com/Knighthawk-Leo/WorkShopTemplate

### Thanks to @https://github.com/Knighthawk-Leo/WorkShopTemplate for the repository and the session

## Prompt Engineering Patterns

1. Role Prompting - Make the model assume itself as someone or something
2. Step by Step Thinking - Give enough context with only few prompts to save space in context
3. Structured Outputs - The output from the LLM should be in the correct structure and format that the user needs. Ex - Pick a number between 10 to 100
   Answer should be 90 ( just the number and not an entire line or paragraph like - I pick the number 90 - the line makes it difficult for the user to extract his desired output. )
4. Setting Constraints and Guardrails - Telling the LLM what not to do, what answers not to give.

# Multi-Agent System Workshop

A simple, hands-on multi-agent system built from scratch. Perfect for learning how agents work and adding your own!

## 🎯 What This Is

This is a simplified multi-agent system where:

- **Agents** are independent components that handle specific tasks
- **Orchestrator** routes queries to the right agent
- **Base Classes** make it easy to create new agents
- **API** provides a simple interface to interact with agents

## 🚀 Quick Start

### 1. Setup

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set your Gemini API key
export GEMINI_API_KEY="your-api-key-here"
```

### 2. Run the Server

```bash
python main.py
```

The API will be available at `http://localhost:8000`

### 3. Open the UI

Open `green.html` in your browser to interact with the system.

## 📁 Project Structure

```
Python-Vanila-MultiAgent-Workshop/
├── agents/
│   ├── __init__.py              # Package initialization
│   ├── base_agent.py            # Base class for all agents
│   ├── orchestrator.py          # Routes queries to agents
│   ├── code_interpreter.py      # Example: Data analysis agent
│   ├── answer_synthesiser.py    # Example: Answer formatting agent
│   └── sample_custom_agent.py   # Template for creating new agents
├── main.py                      # FastAPI server
├── requirements.txt             # Dependencies
├── green.html                   # Web UI
└── README.md                    # This file
```

## 🤖 How Agents Work

### Agent Lifecycle

1. **User sends a query** → API receives it
2. **Orchestrator determines** which agent should handle it
3. **Agent processes** the query and returns a result
4. **Agent can route** to another agent (or return final answer)
5. **Result is returned** to the user

### Agent Structure

Every agent must:

- Inherit from `BaseAgent`
- Implement `get_capabilities()` - describe what it can do
- Implement `process()` - handle the main logic
- Return an `AgentResult` with success, data, and optionally next_agent
