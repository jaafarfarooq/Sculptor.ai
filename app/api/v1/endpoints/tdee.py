from fastapi import APIRouter
from app.models.tdee_model import BMR
from app.models.workout_request import WorkoutRequest    
from app.services.calculate_tdee_with_macros import calculate_tdee_with_macros
from app.services.exercise_recomendar import get_chatgpt_response

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

@router.post("/exercise_recommender")
async def exercise_recommender(data : WorkoutRequest):
    return get_chatgpt_response(
        data.sex,
        data.age,
        data.height,
        data.weight,
        data.hypertension,
        data.diabetes,
        data.injuries,
        data.body_fat,
        data.primary_fitness_goal,
        data.preferred_fitness_type,
        data.experience_level,
        data.days,
        data.gym_access,
        data.available_equipment,
        data.workout_duration
    )
