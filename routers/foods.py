from fastapi import APIRouter
from schemas.foods import GaragePost, GarageResponse

food_router = APIRouter()


@food_router.post('/', response_model=GarageResponse)
async def post_food():
    pass


@food_router.get('/')
async def get_foods():
    pass


@food_router.delete('/{food_id}')
async def delete_food():
    pass


@food_router.get('/recipe')
async def get_recipe():
    pass
