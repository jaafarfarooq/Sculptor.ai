from pydantic import BaseModel, Field
from enum import Enum

class GenderEnum(str, Enum):
    male = "male"
    female = "female"

class ActivityLevelEnum(str, Enum):
    sedentary = "sedentary"
    light = "light"
    moderate = "moderate"
    active = "active"
    athlete = "athlete"

class GoalEnum(str, Enum):
    bulk = "bulk"
    cut = "cut"
    maintain = "maintain"

class BMR(BaseModel):
    weight_kg: float = Field(..., description="Weight in kilograms")
    height_cm: float = Field(..., description="Height in centimeters")
    age: int = Field(..., description="Age in years")
    gender: GenderEnum
    activity_level: ActivityLevelEnum
    goal: GoalEnum
