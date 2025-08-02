from fastapi import APIRouter
from app.models import UserProfile
from app.services import generate_recommendation

router = APIRouter()

@router.post("/recommend")
def get_recommendation(profile: UserProfile):
    return generate_recommendation(profile)
