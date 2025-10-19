<script setup lang="ts">
import Cell from '@/components/TicTacToe/Cell.vue'
import type { Player } from '@/types/types'
import { ref, watch } from 'vue'
import { useTurn, useWS } from '@/composables'

const props = defineProps({
  data: Object
})

const player_1 = ref<Player>({
  id: 'player_1',
  order: 1,
})

const player_2 = ref<Player>({
  id: 'player_2',
  order: 2,
})

const field = ref(Array(9).fill(null))
const current_player = ref(player_1.value)

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
