from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.models.database import Base
from backend.models.document import Document

class Topic(Base):

    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True)

    document_id = Column(Integer, ForeignKey("documents.id"))

    chapter = Column(String)
    topic = Column(String)
    subtopic = Column(String)

    page_start = Column(Integer)
    page_end = Column(Integer)

    document = relationship("Document")