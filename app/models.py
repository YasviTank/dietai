from pydantic import BaseModel
from typing import List

class UserProfile(BaseModel):
    name: str
    age: int
    health_conditions: List[str]
    dietary_preferences: List[str]
    preferred_cuisines: List[str]
