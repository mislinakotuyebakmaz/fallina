from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .base import Base

class FortuneReading(Base):
    __tablename__ = "fortune_readings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    fortune_type = Column(String, nullable=False)  # coffee, tarot, palm, astrology
    image_url = Column(String, nullable=True)
    ai_response = Column(Text, nullable=False)
    is_pro_reading = Column(String, nullable=False, default="free")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="fortune_readings")
    chats = relationship("FortuneChat", back_populates="fortune_reading")