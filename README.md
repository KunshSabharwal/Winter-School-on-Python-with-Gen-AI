## Forked from @https://github.com/Knighthawk-Leo/WorkShopTemplate

### Thanks to @https://github.com/Knighthawk-Leo/WorkShopTemplate for the repository and the session

## Prompt Engineering Patterns

1. Role Prompting - Make the model assume itself as someone or something
2. Step by Step Thinking - Give enough context with only few prompts to save space in context
3. Structured Outputs - The output from the LLM should be in the correct structure and format that the user needs. Ex - Pick a number between 10 to 100
   Answer should be 90 ( just the number and not an entire line or paragraph like - I pick the number 90 - the line makes it difficult for the user to extract his desired output. )
4. Setting Constraints and Guardrails - Telling the LLM what not to do, what answers not to give.

#### Zero-Shot prompting -We give the LLM a direct instruction or question to perform a task without providing any examples of how to do it, relying entirely on its pre-trained knowledge

#### Few-Shot prompting - We provide the LLM with a few examples (typically 2-5) of input/output pairs within the prompt itself, teaching it the desired task, format, or style without needing full retraining

#### Chain of Thought prompting - We guides the LLM to solve complex problems by breaking them down into intermediate reasoning steps, mimicking human thought, rather than jumping straight to an answer, which improves accuracy and transparency

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
venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Set your Gemini API key
$env:GEMINI_API_KEY="YOUR_API_KEY_HERE"
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

### This currently has 3 agents: (3rd Agent Data Visualizer created and added successfully!)

Available Agents -

- CodeInterpreter

  - Execute Python code for data analysis
  - Load and analyze CSV files
  - Perform statistical analysis

- AnswerSynthesiser

  - Answer general questions
  - Synthesize final answers from analysis
  - Format responses with markdown
  - Handle conversational queries

- DataVisualizer
  - Purpose: Generate plots/charts from CSV or numerical outputs
  - Features:
    - Bar, line, scatter, or histogram plots
    - Optionally output plots as base64 images for API responses
    - Works with CodeInterpreter’s outputs
  - Use-case: Turn raw numbers into visual insights for reports or dashboards

### Agents dont follow any fixed standards, they often create and follow their own

1. Workflow - The flow of data and the generated outputs from one to the other agent from the time the input is given, till the time the final output is generated.
2. HandOff Routing - Passing the parcel - Passes the data and the current state of the output to the other agent. Free to call oher agents for the future works
3. Agents as Tools - Agents are tools that should be able to extract the required inputs from the given prompt and pass that to the agent which acts as a tool to execute the task.
4. Reflection - The agent learns overtime and fixes the errors that it makes. It may sometime get infinitely stuck in improvement so we set a parameter that is the MaximumDepthOfAnAgent.
5. LLM as a Judge - The LLM should be able to select the best response from the agent to get the most accurate response. The issue here is that we assume the biggest/largest model as the best one due to which there is a bias and we may get incorrect answer from that agent.
6. Planning - Create a plan and make small checkpoints that are completed and ticked off over time the agent works and the work is done.
7. The Supervisor - The supervisor makes the call of which agent will work and orchastrates the entire process to get the output, not explicitly doing anything to solve the problem/query itself.
8. Multi-Agent Collaboration - Multiple agents for multiple tasks and all agents have separate capabilities. We maintain another variable called 'state' to maintain the state of the agent at present to decide which agent gets the memory.

## RAG Systems (Retrieval-Augmented Generation)

- Thanks to @JaskiratSingh for the session on RAG systems and the hands on coding for the Winter School Python with Gen AI_Day-2_Rag-agent Colab notebook.

### RAG is a framework and not an architecutre

- Framework that combines the question and the relevant chunks to obtain the answer.
- The asked question by the user is checked by retriever that retrieves that fixed data from the knowledge base (which is separated and broken down into chunks and embedded into numerical values, each numerical value of a word is mapped to the word itself, which finally passes the word chunks) to the LLM instead of the complete knowledge base at once. Only the relevant chunk of the knowledge base is passed (Context Window Problem - fixed LLM memory causes LLM's to forget crucial details in long chats/conversations leading to errors, hallucinations, and decreased accuracy)
- There is a slight ovelapping between chunks to build a better connection between them and the selected chunk provides slight context about its previous and next chunks.
- In the retriever, the number of chunks to retrieve is determined by the top-k parameter, a value that is set by the system designer, not determined automatically by the system itself. A small k risks missing crucial info, while a large k adds computational cost and noise.
- User query, relevant chunks, system instruction are the 3 most important parts of the context builder (prompt assembly).
- RAG's take multiple types of data - text, images (text extracted by OCR), videos (text extracted from audio transcripts) and many other types of data.

### Notion document - https://www.notion.so/RAG-Pipeline-with-LangChain-Google-Gemini-and-Agents-2e514dc3f1ec8051835cfb236da43fa9

### Colab Notebook Copy created and added to drive
