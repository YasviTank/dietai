from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router

app = FastAPI(title="Diet AI")

# Allow all origins for testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # <-- in production, restrict this!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
