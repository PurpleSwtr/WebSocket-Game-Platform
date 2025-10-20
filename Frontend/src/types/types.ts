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

// Рудимент по факту, потому что я понял что получать это можно прямо от окна.. Но иногда может и сможет пригодится
export const FrontendURL = "192.168.1.67:5173/api_v1/"
export const BackendURL = "localhost:8000/api_v1/"
export const WebSocketURL = "websocket/ws/"
