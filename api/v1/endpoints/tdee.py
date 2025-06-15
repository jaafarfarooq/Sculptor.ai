from fastapi import APIRouter
from app.models.tdee_model import BMR
from app.services.calculate_tdee_with_macros import calculate_tdee_with_macros

router = APIRouter()

@router.post("/tdee")
async def tdee_calculator(data: BMR):
    return calculate_tdee_with_macros(
        data.weight_kg,
        data.height_cm,
        data.age,
        data.gender,
        data.activity_level,
        data.goal
    )
