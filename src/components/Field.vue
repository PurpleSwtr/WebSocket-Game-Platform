<script setup lang="ts">
import Cell from '@/components/Cell.vue'
import type { Player } from '@/types/types'
import { ref } from 'vue'
import { useTurn } from '@/composables'

const player_1 = ref<Player>({
  id: 'player_1',
  order: 1,
  name: 'Adam',
})

const player_2 = ref<Player>({
  id: 'player_2',
  order: 2,
  name: 'Robin',
})

const field = ref(Array(9).fill(null))

const current_player = ref(player_1.value)

const onCellClick = (cell: number, player: Player, field: any) => {
  field[cell] = useTurn(player)
  console.log((field[cell] = useTurn(current_player.value)))
  current_player.value = current_player.value.order == 1 ? player_2.value : player_1.value
  console.log(current_player.value)
}
</script>

<template>
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
