from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .base import Base

class FortuneChat(Base):
    __tablename__ = "fortune_chats"

    id = Column(Integer, primary_key=True, index=True)
    fortune_reading_id = Column(Integer, ForeignKey("fortune_readings.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    question = Column(Text, nullable=False)
    ai_response = Column(Text, nullable=False)
    question_count = Column(Integer, default=1)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    fortune_reading = relationship("FortuneReading", back_populates="chats")
    user = relationship("User", back_populates="fortune_chats")