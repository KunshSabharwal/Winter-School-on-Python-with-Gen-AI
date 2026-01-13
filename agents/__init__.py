"""
Multi-Agent System Package
"""

from .base_agent import BaseAgent, AgentResult, Message
from .code_interpreter import CodeInterpreterAgent
from .answer_synthesiser import AnswerSynthesiserAgent

# Import your custom agents here
# from .your_custom_agent import YourCustomAgent

__all__ = [
    "BaseAgent",
    "AgentResult",
    "Message",
    "CodeInterpreterAgent",
    "AnswerSynthesiserAgent",
]
