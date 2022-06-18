from datetime import date
from pydantic import BaseModel


class Food(BaseModel):
    food_id: str
    name: str


class Garage(BaseModel):
    quantity: int
    limit_at: date


class GaragePost(BaseModel):
    name: str
    quantity: int
    limit_at: date


class GarageResponse(BaseModel):
    food_id: str
    name: str
    quantity: int
    limit_at: date
