from fastapi import FastAPI
from app.api.v1.endpoints import tdee

app = FastAPI()

app.include_router(tdee.router, prefix="/api/v1", tags=["TDEE"])
