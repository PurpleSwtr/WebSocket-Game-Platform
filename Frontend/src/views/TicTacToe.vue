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


</script>
<template>
  TicTacToe {{ $route.params.id }}
  <main class="flex justify-center items-center min-h-screen">
    <Field :data="ws_data" :session_id="`${$route.params.id}`"/>
  </main>
</template>

<style scoped>

</style>
