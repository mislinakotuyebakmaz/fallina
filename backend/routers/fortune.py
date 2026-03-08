from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import get_db
from middleware.auth_middleware import get_current_user
from services.ai_service import get_coffee_fortune
from models.user import User
from models.fortune_reading import FortuneReading

router = APIRouter(prefix="/fortune", tags=["fortune"])

class CoffeeFortuneRequest(BaseModel):
    image_url: str

@router.post("/coffee")
def coffee_fortune(
    request: CoffeeFortuneRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    ai_response = get_coffee_fortune(
        image_url=request.image_url,
        is_pro=current_user.is_pro
    )

    reading = FortuneReading(
        user_id=current_user.id,
        fortune_type="coffee",
        image_url=request.image_url,
        ai_response=ai_response,
        is_pro_reading="pro" if current_user.is_pro else "free"
    )
    db.add(reading)
    db.commit()
    db.refresh(reading)

    return {
        "id": reading.id,
        "fortune_type": "coffee",
        "ai_response": ai_response,
        "is_pro": current_user.is_pro
    }