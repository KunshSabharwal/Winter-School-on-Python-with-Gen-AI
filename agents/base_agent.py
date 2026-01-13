"""
Base Agent Class - All agents inherit from this
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Message:
    """Represents a message in the conversation"""

    role: str  # 'user', 'agent', 'system'
    content: str
    metadata: Dict[str, Any] = None
    timestamp: datetime = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()
        if self.metadata is None:
            self.metadata = {}


@dataclass
class AgentResult:
    """Result returned by an agent after processing"""

    success: bool
    data: Any
    message: str
    agent_name: str
    next_agent: Optional[str] = None  # Which agent should handle this next
    metadata: Dict[str, Any] = None

    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}


class BaseAgent(ABC):
    """
    Base class for all agents.
    To create a new agent, inherit from this class and implement:
    - process() method: handles the main logic
    - get_capabilities() method: returns list of what the agent can do
    """

    def __init__(self, name: str, api_key: str):
        self.name = name
        self.api_key = api_key
        self.conversation_history: List[Message] = []

    @abstractmethod
    async def process(self, input_data: Dict[str, Any]) -> AgentResult:
        """
        Process the input and return a result.
        This is the main method you need to implement.

        Args:
            input_data: Dictionary containing:
                - query: str - The user's query
                - context: Dict - Context from previous agents
                - files: Dict - Uploaded files (filename -> filepath)

        Returns:
            AgentResult with success, data, message, and optionally next_agent
        """
        pass

    @abstractmethod
    def get_capabilities(self) -> List[str]:
        """
        Return a list of capabilities this agent has.
        Used for routing and displaying agent info.
        """
        pass

    def add_to_history(self, message: Message):
        """Add a message to conversation history"""
        self.conversation_history.append(message)

    def get_history(self) -> List[Message]:
        """Get conversation history"""
        return self.conversation_history

    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
