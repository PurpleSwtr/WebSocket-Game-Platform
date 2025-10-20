<script setup lang="ts">
import Cell from '@/components/TicTacToe/Cell.vue'
// import type { Player } from '@/types/types'
// import { ref, watch } from 'vue'
// import { useTurn, useWS } from '@/composables'
// import { usePlayerStore } from '@/stores/player';

const props = defineProps<{
  data: (string | null)[][]
}>()
console.log(props.data)
const onCellClick = () => {

}

const onGameUpdate = () => {

}

// const field = ref(props.data["field"])

</script>

<template>
  <!-- <div class="absolute top-30">{{ current_player.id }}</div> -->
  <div class="grid grid-cols-3 gap-[0.1px]">
    <!-- <Cell
      v-for="(cellSymbol, index) in field"
      :key="index"
      :cell_id="index"
      :symbol="cellSymbol"
      @cellClick="onCellClick()"
    ></Cell> -->
  </div>
</template>

<style scoped></style>
