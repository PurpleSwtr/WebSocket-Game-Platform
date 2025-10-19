<script setup lang="ts">
import Cell from '@/components/TicTacToe/Cell.vue'
import type { Player } from '@/types/types'
import { ref, watch } from 'vue'
import { useTurn, useWS } from '@/composables'

const props = defineProps<{
  data: any
  session_id: string
}>()



const onCellClick = () => {
  const testMessage = {
    user: '3fa85f64-5717-4562-b3fc-2c963f66afa6',
    action: 'prepared',
  }
  useWS(props.session_id, testMessage, props.data)
}

const onGameUpdate = () => {

}

const field = ref(props.data["field"])

</script>

<template>
  <!-- <div class="absolute top-30">{{ current_player.id }}</div> -->
  <div class="grid grid-cols-3 gap-[0.1px]">
    <Cell
      v-for="(cellSymbol, index) in field"
      :key="index"
      :cell_id="index"
      :symbol="cellSymbol"
      @cellClick="onCellClick()"
    ></Cell>
  </div>
</template>

<style scoped></style>
