<script setup lang="ts">
import Cell from '@/components/TicTacToe/Cell.vue'
import { onMounted, ref, watch } from 'vue';
// import type { Player } from '@/types/types'
// import { ref, watch } from 'vue'
// import { useTurn, useWS } from '@/composables'
// import { usePlayerStore } from '@/stores/player';

const props = defineProps<{
  data: (string | null)[][]
}>()

const field = ref<(string | null)[]>([])
field.value = props.data.flat()

console.log(props.data)

const emit = defineEmits(['fieldClick'])

const onCellClick = (cellData: {id: number}) => {
  console.log(`Field emit: ${cellData.id}`)
  const map: {[key: number]: [number, number]} = {
    0: [0,0], 1: [0,1], 2: [0,2],
    3: [1,0], 4: [1,1], 5: [1,2],
    6: [2,0], 7: [2,1], 8: [2,2],
  }

  const index = map[cellData.id]

  if (index) {
    const [row, col] = index
    emit('fieldClick', {
      row: row,
      col: col
    })
  }
}

watch(props.data, (newData) => {
  if (newData) {
    field.value = newData.flat()
  }
})


</script>

<template>
  <!-- <div class="absolute top-30">{{ current_player.id }}</div> -->
  <div class="grid grid-cols-3 gap-[0.1px]">
    <Cell
      v-for="(cellSymbol, index) in field"
      :key="index"
      :cell_id="index"
      :symbol="cellSymbol"
      @cellClick="onCellClick"
    ></Cell>
  </div>
</template>

<style scoped></style>
