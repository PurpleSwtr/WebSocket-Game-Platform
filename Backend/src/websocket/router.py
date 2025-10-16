import json
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import List
from ..core.models import active_sessions
router = APIRouter(prefix="/websocket", tags=["Веб-сокет"])

class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[str, List[WebSocket]] = {}
    
    async def connect(self, websocket: WebSocket, session_id: str):
        await websocket.accept()
        if session_id not in self.active_connections:
            self.active_connections[session_id] = []
        self.active_connections[session_id].append(websocket)
    
    def disconnect(self, websocket: WebSocket, session_id: str):
        if session_id in self.active_connections:
            self.active_connections[session_id].remove(websocket)
            if not self.active_connections[session_id]:
                del self.active_connections[session_id]
    
    async def broadcast_to_session(self, game_data: str, session_id: str):
        if session_id in self.active_connections:
            for connection in self.active_connections[session_id]:
                await connection.send_text(game_data)

manager = ConnectionManager()
# Примерное сообщение с форнтенда:
# {"user": "uuid", "action": "move", "row": 1, "col": 2}

@router.websocket("/ws/{session_id}")
async def websocket_endpoint(websocket: WebSocket, session_id: str):
    await manager.connect(websocket, session_id)
    try:
        while True:
            data = await websocket.receive_text()
            move_data = json.loads(data)
            current_session = active_sessions.get(session_id)
            player_id = move_data.user
            await manager.broadcast_to_session(data, session_id)
    except WebSocketDisconnect:
        manager.disconnect(websocket, session_id)