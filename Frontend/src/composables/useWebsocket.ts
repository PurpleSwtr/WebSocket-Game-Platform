// import { useWebSocket } from '@vueuse/core'
import { BackendURL, WebSocketURL } from '@/types/types'
import type { Ref } from 'vue'

// NOTE: Какой-то перегруженный для мего случая найденный готовый способ, буду писать с нуля сам
// export const useWS = (session_id: string) => {
//   const { status, data, send, open, close } = useWebSocket(`ws://${BackendURL}${WebSocketURL}${session_id}`)
//   return { status, data, send, open, close }
// }

let ws: WebSocket | null = null;

export const disconnectWS = () => {
    if (ws) {
        ws.onclose = null;
        ws.close();
        ws = null;
        console.log("WebSocket disconnected.");
    }
};

export const initWS = (session_id: string, dataRef: Ref<any>) => {
  if (ws) {
    return;
  }

  ws = new WebSocket(`ws://${BackendURL}${WebSocketURL}${session_id}`)

  ws.onopen = function (event) {
    console.log("WebSocket init", session_id)
  }

  ws.onmessage = function (event) {
    console.log(event.data);
    try {
      dataRef.value = JSON.parse(event.data)
    } catch {
      dataRef.value = event.data
    }
  }

  ws.onerror = function (error) {
    console.error('WebSocket Error:', error)
  }

    ws.onclose = function () {
    console.log("WebSocket connection closed.");
    ws = null;
  }
}

export const sendWS = (query: object) => {
    if (ws && ws.readyState === WebSocket.OPEN) {
        ws.send(JSON.stringify(query));
    } else {
        console.error("WebSocket не подключен.");
    }
}
