from fastapi import FastAPI
from pydantic import BaseModel
from app.config import settings
from fastapi.middleware.cors import CORSMiddleware

from app.calculator import calculate_macros
from app.schemas.nutrition import (
    NutritionRequest,
    NutritionResponse
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": f"{settings.app_name} API is running",
        "version": settings.app_version
        }

@app.post("/calculate", response_model=NutritionResponse)
def calculate(data: NutritionRequest):
    result = calculate_macros(
        weight = data.weight,
        height = data.height,
        age = data.age,
        activity_level = data.activity_level,
        goal = data.goal
    )
    return result

