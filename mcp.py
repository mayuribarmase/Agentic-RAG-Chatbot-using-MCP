# mcp.py

import uuid
from typing import Any, Dict

class MCPMessage:
    def __init__(self, sender: str, receiver: str, type_: str, payload: Dict[str, Any], trace_id: str = None):
        self.sender = sender
        self.receiver = receiver
        self.type = type_
        self.payload = payload
        self.trace_id = trace_id or str(uuid.uuid4())

    def to_dict(self):
        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "type": self.type,
            "trace_id": self.trace_id,
            "payload": self.payload,
        }

    @staticmethod
    def from_dict(data: dict):
        return MCPMessage(
            sender=data["sender"],
            receiver=data["receiver"],
            type_=data["type"],
            payload=data["payload"],
            trace_id=data.get("trace_id")
        )

    def __repr__(self):
        return str(self.to_dict())
