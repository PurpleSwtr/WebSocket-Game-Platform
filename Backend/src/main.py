from typing import Annotated

from fastapi import FastAPI, Form
# from fastapi.datastructures import FormData

from .core.models import Player, GameSession
from .api import main_router

app = FastAPI()
app.include_router(main_router, prefix="/api_v1")

# router = APIRouter(prefix='/users', tags='Пользователи')

