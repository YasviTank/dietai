from pydantic import BaseModel
from typing import List, Optional

class UserProfile(BaseModel):
    name: str
    age: int
    health_conditions: List[str]
    dietary_preferences: List[str]
    preferred_cuisines: List[str]
    allergies: Optional[List[str]] = []
    avoid_foods: Optional[List[str]] = []
    meal_types: List[str] = []  

