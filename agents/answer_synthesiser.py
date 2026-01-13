"""
Answer Synthesiser Agent - Simple agent that provides final answers
"""

import google.generativeai as genai
from typing import Dict, Any, List
from .base_agent import BaseAgent, AgentResult


class AnswerSynthesiserAgent(BaseAgent):
    """Simple agent that synthesizes final answers for users"""

    def __init__(self, api_key: str):
        super().__init__(name="AnswerSynthesiser", api_key=api_key)
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def get_capabilities(self) -> List[str]:
        return [
            "Answer general questions",
            "Synthesize final answers from analysis",
            "Format responses with markdown",
            "Handle conversational queries",
        ]

    async def process(self, input_data: Dict[str, Any]) -> AgentResult:
        query = input_data.get("query", "")
        context = input_data.get("context", {})

        prompt = self._build_prompt(query, context)

        try:
            response = self.model.generate_content(prompt)
            response_text = response.text

            return AgentResult(
                success=True,
                data={
                    "answer": response_text,
                    "formatted_answer": response_text,
                },
                message="Answer synthesized successfully",
                agent_name=self.name,
                next_agent=None,  # This is usually the final agent
            )
        except Exception as e:
            return AgentResult(
                success=False,
                data={"error": str(e)},
                message=f"Error: {str(e)}",
                agent_name=self.name,
            )

    def _build_prompt(self, query: str, context: Dict[str, Any]) -> str:
        has_code_results = context.get("codeinterpreter_data") is not None

        if has_code_results:
            ci_data = context.get("codeinterpreter_data", {})
            prompt = f"""You are an AI assistant. Based on the analysis results, provide a clear answer.

User Query: {query}

Analysis Results:
"""
            if ci_data.get("analysis"):
                prompt += f"{ci_data['analysis']}\n\n"
            if ci_data.get("results"):
                for result in ci_data["results"]:
                    if result.get("output"):
                        prompt += f"{result['output']}\n"

            prompt += """
Instructions:
1. Provide a clear, user-friendly answer
2. Use markdown formatting
3. Focus on insights, not technical details
4. Be conversational and easy to understand

Provide your answer:
"""
        else:
            prompt = f"""You are a helpful AI assistant. Answer the user's question clearly.

User Query: {query}

Instructions:
1. Provide a clear, accurate answer
2. Use markdown formatting
3. Be conversational but professional

Provide your answer:
"""

        return prompt
