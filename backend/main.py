from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.upload import router as upload_router
from backend.api.topics import router as topics_router
from backend.api.toc import router as toc_router
from backend.api.explain import router as explain_router
from backend.api.lesson import router as lesson_router


app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(upload_router)
app.include_router(topics_router)
app.include_router(toc_router)
app.include_router(explain_router)
app.include_router(lesson_router)


@app.get("/")
def root():
    print("[API] Root endpoint called")
    return {"message": "Textbook Tutor API running"}