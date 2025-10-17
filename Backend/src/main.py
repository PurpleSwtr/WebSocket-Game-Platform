from typing import Annotated

from fastapi import FastAPI, Form
# from fastapi.datastructures import FormData

from .core.models import Player, GameSession
from .api import main_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

# CORS КОНИФГ
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(main_router, prefix="/api_v1")

# router = APIRouter(prefix='/users', tags='Пользователи')

