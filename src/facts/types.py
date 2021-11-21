from typing import List
from pydantic import BaseModel


class Position(BaseModel):
    lat: float
    lng: float


class FactWithoutId(BaseModel):
    name: str
    description: str
    pos: Position


class Fact(FactWithoutId):
    fact_id: str


Facts = List[Fact]
