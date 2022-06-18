from datetime import date
from fastapi import HTTPException
from sqlalchemy.orm.session import Session
from db.model import Food, Garage
from schemas.foods import GarageResponse


def create_food(db: Session, name: str, quantity: int, limit_at: date):
    same_name_food = db.query(Food).filter(Food.name == name).first()
    if same_name_food is not None:
        raise HTTPException(
            status_code=400, detail="this food is already existed")

    garage_orm = Garage(
        quantity=quantity,
        limit_at=limit_at
    )

    db.add(garage_orm)
    db.commit()
    db.refresh(garage_orm)

    food = GarageResponse.from_orm(garage_orm)
