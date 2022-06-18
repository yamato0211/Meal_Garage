from datetime import date
from tkinter.font import _FontDescription
from fastapi import HTTPException
from sqlalchemy.orm.session import Session
from db.model import Food, Garage
from schemas.foods import GarageResponse, Foods


def create_food(db: Session, name: str, quantity: int, limit_at: date):
    same_name_food = db.query(Food).filter(Food.name == name).first()
    if same_name_food is None:
        food_orm = Food(
            name=name
        )
        db.add(food_orm)
        db.commit()
        db.refresh(food_orm)
        food = Foods.from_orm(food_orm)
        return {
            "food_id": food,
            "name": name,
            "quantity": quantity,
            "limit_at": limit_at
        }
    else:
        return{
            "food_id": food,
            "name": name,
            "quantity": quantity,
            "limit_at": limit_at
        }


def get_foods_list(db: Session) -> GarageResponse:
