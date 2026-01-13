"""
Sample Custom Agent Template
This file shows you how to create your own agent!

To use this agent:
1. Copy this file and rename it (e.g., my_agent.py)
2. Replace "SampleCustomAgent" with your agent name
3. Implement the process() and get_capabilities() methods
4. Import and register it in orchestrator.py
"""

import google.generativeai as genai
from typing import Dict, Any, List
from .base_agent import BaseAgent, AgentResult


class SampleCustomAgent(BaseAgent):
    """
    This is a template for creating your own agent.

    Steps to create your agent:
    1. Inherit from BaseAgent
    2. Implement get_capabilities() - describe what your agent can do
    3. Implement process() - this is where your agent's logic goes
    4. Return an AgentResult with success, data, message, and optionally next_agent
    """

    def __init__(self, api_key: str):
        # Call parent constructor with your agent's name
        super().__init__(name="SampleCustomAgent", api_key=api_key)

        # Initialize Gemini if you need AI capabilities
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.0-flash")

        # Add any other initialization here
        # self.my_data = {}

    def get_capabilities(self) -> List[str]:
        """
        Return a list of what this agent can do.
        This is used for routing and displaying agent info.
        """
        return [
            "Do something specific",
            "Handle certain types of queries",
            "Process specific data",
        ]

    async def process(self, input_data: Dict[str, Any]) -> AgentResult:
        """
        This is the main method where your agent's logic goes.

        Args:
            input_data: Dictionary containing:
                - query: str - The user's query
                - context: Dict - Context from previous agents
                - files: Dict - Uploaded files (filename -> filepath)

        Returns:
            AgentResult with:
                - success: bool - Whether processing succeeded
                - data: Any - The result data
                - message: str - A message about what happened
                - next_agent: Optional[str] - Which agent to call next (or None to stop)
        """
        query = input_data.get("query", "")
        context = input_data.get("context", {})
        files = input_data.get("files", {})

        try:
            # ============================================
            # YOUR AGENT LOGIC GOES HERE
            # ============================================

            # Example: Use Gemini to process the query
            prompt = f"""You are a helpful assistant. Answer this question: {query}
            
            Provide a clear, concise answer:
            """

            response = self.model.generate_content(prompt)
            answer = response.text

            # ============================================
            # Return the result
            # ============================================
            return AgentResult(
                success=True,
                data={
                    "answer": answer,
                    "processed_query": query,
                },
                message="Processing completed successfully",
                agent_name=self.name,
                next_agent=None,  # None means this is the final agent
                # Or route to another agent:
                # next_agent="AnswerSynthesiser",
            )

        except Exception as e:
            # Handle errors
            return AgentResult(
                success=False,
                data={"error": str(e)},
                message=f"Error processing: {str(e)}",
                agent_name=self.name,
            )


# ============================================
# EXAMPLE: Simple Calculator Agent
# ============================================
class CalculatorAgent(BaseAgent):
    """A simple example agent that does basic math"""

    def __init__(self, api_key: str):
        super().__init__(name="CalculatorAgent", api_key=api_key)

    def get_capabilities(self) -> List[str]:
        return [
            "Perform basic calculations",
            "Add, subtract, multiply, divide numbers",
        ]

    async def process(self, input_data: Dict[str, Any]) -> AgentResult:
        query = input_data.get("query", "")

        # Simple example: extract numbers and calculate
        # In a real agent, you'd use AI or more sophisticated parsing
        try:
            # This is just a simple example - you'd make this smarter!
            if "add" in query.lower() or "+" in query:
                # Extract numbers and add them
                # (This is simplified - real implementation would be more robust)
                numbers = [int(s) for s in query.split() if s.isdigit()]
                if len(numbers) >= 2:
                    result = sum(numbers)
                    return AgentResult(
                        success=True,
                        data={"result": result, "operation": "addition"},
                        message=f"Calculated: {result}",
                        agent_name=self.name,
                        next_agent="AnswerSynthesiser",
                    )
        except Exception as e:
            pass

        return AgentResult(
            success=False,
            data={"error": "Could not parse calculation"},
            message="Could not perform calculation",
            agent_name=self.name,
        )
