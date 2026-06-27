from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.calculator import calculate_macros
from app.schemas.nutrition import (
    NutritionRequest,
    NutritionResponse
)

app = FastAPI(title=settings.app_name, version=settings.app_version)
static_dir = Path(__file__).resolve().parent / "static"

app.mount("/static", StaticFiles(directory=static_dir), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return FileResponse(static_dir / "index.html")

@app.get("/health")
def health():
    return {"status": "ok"}

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
