<script setup lang="ts">
import Cell from '@/components/TicTacToe/Cell.vue'
import type { Player } from '@/types/types'
import { ref, watch } from 'vue'
import { useTurn, useWS } from '@/composables'

const player_1 = ref<Player>({
  id: 'player_1',
  order: 1,
})

const player_2 = ref<Player>({
  id: 'player_2',
  order: 2,
})

let ws_data = ref<any>({})

const field = ref(Array(9).fill(null))
const current_player = ref(player_1.value)

const onCellClick = (cell: number, player: Player, field: any) => {
  const testMessage = {
    user: '3fa85f64-5717-4562-b3fc-2c963f66afa6',
    action: 'prepared',
  }
  useWS('b3959e78-b023-4287-aaf7-c66e7b46abc8', testMessage, ws_data)
}

watch(ws_data, (newData) => {
  console.log(newData)
})

</script>

<template>
  <div class="absolute top-30">{{ current_player.id }}</div>
  <div class="grid grid-cols-3 gap-[0.1px]">
    <Cell
      v-for="(cellSymbol, index) in field"
      :key="index"
      :cell_id="index"
      :symbol="cellSymbol"
      @cellClick="onCellClick(index, player_1, field)"
    ></Cell>
  </div>
</template>

<style scoped></style>
