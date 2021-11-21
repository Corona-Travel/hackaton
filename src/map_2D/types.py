from typing import List
from pydantic import BaseModel


class Position(BaseModel):
    lat: float
    lng: float


class Marker(BaseModel):
    name: str
    place_id: str
    pos: Position


Markers = List[Marker]
