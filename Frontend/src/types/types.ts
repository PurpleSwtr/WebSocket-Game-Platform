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

export interface TicTacToeData {
  field: [[any]]
  current_turn: string,
  winner: string,
  draw: boolean,
}

export interface MessageBase {
  user: string;
  action: string;
}

export interface MessageExtensions {
  row?: number;
  cel?: number;
  type?: string;
  [key: string]: any;
}

export type MessageWS = MessageBase & MessageExtensions;

export const BackendURL = "localhost:8000/api_v1/"
export const WebSocketURL = "websocket/ws/"
