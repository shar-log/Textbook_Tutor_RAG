from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from datetime import datetime
from backend.models.database import Base


class Summary(Base):

    __tablename__ = "summaries"

    id = Column(Integer, primary_key=True)

    topic_id = Column(Integer, ForeignKey("topics.id"))

    summary = Column(Text)

    generated_at = Column(DateTime, default=datetime.utcnow)