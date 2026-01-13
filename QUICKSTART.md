# Quick Start Guide

## 🚀 Get Running in 3 Steps

### Step 1: Install Dependencies

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Step 2: Set API Key

```bash
export GEMINI_API_KEY="your-api-key-here"
```

Or create a `.env` file:
```
GEMINI_API_KEY=your-api-key-here
```

### Step 3: Run

```bash
python main.py
```

Open `green.html` in your browser and start chatting!

## ➕ Add Your First Agent (5 Minutes)

### 1. Copy the template

```bash
cp agents/sample_custom_agent.py agents/my_first_agent.py
```

### 2. Edit `my_first_agent.py`

Change the class name and implement your logic:

```python
class MyFirstAgent(BaseAgent):
    def __init__(self, api_key: str):
        super().__init__(name="MyFirstAgent", api_key=api_key)
    
    def get_capabilities(self) -> List[str]:
        return ["Does something cool"]
    
    async def process(self, input_data: Dict[str, Any]) -> AgentResult:
        query = input_data.get("query", "")
        
        # Your logic here
        result = f"You asked: {query}"
        
        return AgentResult(
            success=True,
            data={"result": result},
            message="Done!",
            agent_name=self.name,
        )
```

### 3. Register in `orchestrator.py`

```python
from .my_first_agent import MyFirstAgent

# In __init__ method, add:
"MyFirstAgent": MyFirstAgent(api_key),
```

### 4. Test it!

Restart the server and send a message. Your agent is now part of the system!

## 📖 Learn More

See `README.md` for detailed documentation and examples.

