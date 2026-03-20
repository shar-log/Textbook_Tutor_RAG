from backend.models.database import engine
from backend.models.document import Document
from backend.models.topic import Topic
from backend.models.chunk import Chunk
from backend.models.summary import Summary
from backend.models.database import Base

print("[DB INIT] Creating database tables")

Base.metadata.create_all(bind=engine)

print("[DB INIT] Database ready")