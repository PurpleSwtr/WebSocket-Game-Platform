from fastapi import APIRouter 
from ..users.router import router as router_users
from ..websocket.router import router as websocket_router

main_router = APIRouter()

main_router.include_router(router_users)
main_router.include_router(websocket_router)




