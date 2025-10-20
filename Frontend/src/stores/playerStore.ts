import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const usePlayerStore = defineStore('player', {
  state: () => ({
    player_id: ''
  }),
  getters: {
    getPlayerId(state) {
      return state.player_id
    }
  },
  actions: {
    addPlayerId(id: string) {
      this.player_id = id
    }
  }
})
