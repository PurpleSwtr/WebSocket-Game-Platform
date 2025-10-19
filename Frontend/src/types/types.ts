export interface Player {
  id?: string
  order?: number
  name?: string
}

export interface Session {
  session_id: string;
  players: Record<string, Player>;
  status: string;
}

export const BackendURL = "localhost:8000/api_v1/"
export const WebSocketURL = "websocket/ws/"
