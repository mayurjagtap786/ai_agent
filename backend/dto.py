from typing import Any

from pydantic import BaseModel, Json


class Node(BaseModel):
    id: str
    properties: Json[Any]
