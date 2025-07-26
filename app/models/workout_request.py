from pydantic import BaseModel, Field
from typing import List, Optional

class WorkoutRequest(BaseModel):
    sex: str = Field(..., description="User's sex (e.g., 'Male', 'Female')")
    age: int = Field(..., gt=0, description="Age in years")
    height: float = Field(..., gt=0, description="Height in cm")
    weight: float = Field(..., gt=0, description="Weight in kg")
    hypertension: bool = Field(..., description="Does the user have hypertension?")
    diabetes: bool = Field(..., description="Does the user have diabetes?")
    injuries: Optional[str] = Field("", description="Any known injuries or limitations")
    body_fat: Optional[float] = Field(None, gt=0, description="Body fat percentage (optional)")
    primary_fitness_goal: str = Field(..., description="Primary goal (e.g., Weight Loss, Muscle Gain)")
    preferred_fitness_type: str = Field(..., description="Preferred fitness style (e.g., Strength, Cardio)")
    experience_level: str = Field(..., description="User's experience level (Beginner, Intermediate, Advanced)")
    days: int = Field(..., gt=0, le=7, description="Days per week user can train")
    gym_access: bool = Field(..., description="Whether the user has access to a gym")
    available_equipment: List[str] = Field(..., description="List of available equipment")
    workout_duration: int = Field(..., gt=0, description="Workout duration per session in minutes")
