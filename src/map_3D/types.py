from typing import List
from enum import Enum

from pydantic import BaseModel


class Position(BaseModel):
    lat: float
    lng: float


class MarkerType(str, Enum):
    fact = "fact"


class Marker(BaseModel):
    name: str
    marker_id: str
    type: MarkerType
    pos: Position


Markers = List[Marker]
