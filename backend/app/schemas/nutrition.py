from enum import Enum
from pydantic import BaseModel, Field

class ActivityLevel(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class Goal(str, Enum):
    cut = "cut"
    maintain = "maintain"
    bulk = "bulk"

class NutritionRequest(BaseModel):
    weight: float = Field(gt=0, lt=300)
    height: float = Field(gt=50, lt=300)
    age: int = Field(gt=0, lt=120)

    activity_level: ActivityLevel
    goal: Goal

class NutritionResponse(BaseModel):
    calories: int
    protein: int
    fat: int
    carbs: int
    