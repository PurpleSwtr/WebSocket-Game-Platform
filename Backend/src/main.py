from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.router import main_router

print("http://127.0.0.1:8000/docs")

app = FastAPI()

# CORS КОНИФГ
# origins = [
#     "http://localhost:5173",
#     "http://127.0.0.1:5173",
#     "http://192.168.1.67:5173",
#     "http://localhost:8000",
#     "http://127.0.0.1:8000",
# ]

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(main_router, prefix="/api_v1")
