import { ref } from "vue";

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
export const BackendURL = `${window.location.hostname}:8000/api_v1/`
export const WebSocketURL = "websocket/ws/"

// ИКОНКИ
export type IconKey = "fire" | "square" | "lightning" | "cross" | "circle" | "water" | "triangle";

export interface IconData {
  icon: string;
  symbol: string;
  color: string;
  hoverColor: string;
}

export const icons_map = ref<Record<IconKey, IconData>>({
  "fire": { "icon": "fire", "symbol": "R", "color": "bg-red-400", "hoverColor": "hover:bg-red-400" },
  "square": { "icon": "square", "symbol": "O", "color": "bg-orange-300", "hoverColor": "hover:bg-orange-300" },
  "lightning": { "icon": "lightning", "symbol": "Y", "color": "bg-yellow-400", "hoverColor": "hover:bg-yellow-400" },
  "cross": { "icon": "cross", "symbol": "G", "color": "bg-green-500", "hoverColor": "hover:bg-green-500" },
  "circle": { "icon": "circle", "symbol": "L", "color": "bg-cyan-200", "hoverColor": "hover:bg-cyan-200" },
  "water": { "icon": "water", "symbol": "B", "color": "bg-blue-300", "hoverColor": "hover:bg-blue-300" },
  "triangle": { "icon": "triangle", "symbol": "P", "color": "bg-purple-300", "hoverColor": "hover:bg-purple-300" },
});
