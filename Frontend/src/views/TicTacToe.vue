<script setup lang="ts">
import Cell from '@/components/Cell.vue'
import Field from '@/components/TicTacToe/Field.vue'
import { useWS } from '@/composables'
import { usePlayerStore } from '@/stores/playerStore'
// import type { Player } from '@/types/types'
import { ref, watch } from 'vue'
import { useRoute } from 'vue-router'


let ws_data = ref<any>({})

watch(ws_data, (newData) => {
  console.log(newData)
})

const store = usePlayerStore()
const route = useRoute()
const sessionId = route.params.id as string
const testMessage = {
  user: store.player_id,
  action: 'prepared',
}
useWS(sessionId, testMessage, ws_data)
console.log(ws_data.value)


</script>
<template>
  TicTacToe {{ $route.params.id }}
  <main class="flex justify-center items-center min-h-screen">
    <!-- <Field :session_id="`${$route.params.id}`"/> -->
     <Field
        v-if="ws_data.field"
        :data="ws_data.field"
      />
  </main>
</template>

<style scoped>

</style>
