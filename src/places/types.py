from typing import List
from pydantic import BaseModel


class Position(BaseModel):
    lat: float
    lng: float


class PlaceWithoutID(BaseModel):
    name: str
    pos: Position


class Place(PlaceWithoutID):
    place_id: str


Places = List[Place]
