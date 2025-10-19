// import { useWebSocket } from '@vueuse/core'
import { BackendURL, WebSocketURL } from '@/types/types'
import type { Ref } from 'vue'

// NOTE: Какой-то перегруженный для мего случая найденный готовый способ, буду писать с нуля сам
// export const useWS = (session_id: string) => {
//   const { status, data, send, open, close } = useWebSocket(`ws://${BackendURL}${WebSocketURL}${session_id}`)
//   return { status, data, send, open, close }
// }

export const useWS = (session_id: string, query: object, dataRef: Ref<any>) => {
  const ws = new WebSocket(`ws://${BackendURL}${WebSocketURL}${session_id}`)

  ws.onopen = function (event) {
    ws.send(JSON.stringify(query))
  }

  ws.onmessage = function (event) {
    try {
      dataRef.value = JSON.parse(event.data)
    } catch {
      dataRef.value = event.data
    }
  }

  ws.onerror = function (error) {
    console.error('WebSocket Error:', error)
    // Думаю, сомнительное решение, лучше просто в консоль
    // dataRef.value = { error: 'WebSocket error' }
  }
}
