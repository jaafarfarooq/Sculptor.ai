from fastapi import FastAPI
from app.database import engine
from app.models.user import User  # or use from app.models import User
from app.database import Base
from .auth import router as auth_router
from app.api.v1.endpoints import tdee


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router, prefix="/auth")
app.include_router(tdee.router, prefix="/api/v1", tags=["TDEE"])
