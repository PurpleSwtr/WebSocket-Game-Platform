from fastapi import APIRouter
from src.session.router import router as session_router
from src.users.router import router as router_users
from src.websocket.router import router as websocket_router

main_router = APIRouter()

main_router.include_router(router_users)
main_router.include_router(websocket_router)
main_router.include_router(session_router)
