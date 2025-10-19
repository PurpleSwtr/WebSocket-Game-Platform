<script setup lang="ts">
import Cell from '@/components/Cell.vue'
import Field from '@/components/TicTacToe/Field.vue'
import { useWS } from '@/composables'
import type { Player } from '@/types/types'
import { ref, watch } from 'vue'

let ws_data = ref<any>({})

watch(ws_data, (newData) => {
  console.log(newData)
})

const onCellClick = (cell: number, player: Player, field: any) => {
  const testMessage = {
    user: '3fa85f64-5717-4562-b3fc-2c963f66afa6',
    action: 'prepared',
  }
  useWS('b3959e78-b023-4287-aaf7-c66e7b46abc8', testMessage, ws_data)
}

</script>
<template>
  TicTacToe {{ $route.params.id }}
  <main class="flex justify-center items-center min-h-screen">
    <Field />
  </main>
</template>

<style scoped>
.text {
  background-color: green;
  color: white;
}
</style>
