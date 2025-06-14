from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel, Field
from services.calculate_tdee_with_macros import calculate_tdee_with_macros
app = FastAPI()


class BMR(BaseModel):
    weight_kg: float
    height_cm: float
    age: int
    gender: str
    activity_level: str
    goal:str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/TDEE/")
async def TDEE_calculator(s1: BMR):
   return calculate_tdee_with_macros(s1.weight_kg, s1.height_cm, s1.age, s1.gender, s1.activity_level, s1.goal)