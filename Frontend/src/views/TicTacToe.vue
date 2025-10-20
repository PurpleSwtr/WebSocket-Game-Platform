<script setup lang="ts">
import Cell from '@/components/Cell.vue'
import Field from '@/components/TicTacToe/Field.vue'
import WaitingForm from '@/components/ui/WaitingForm.vue'
import { useWS } from '@/composables'
import { usePlayerStore } from '@/stores/playerStore'
import type { MessageWS } from '@/types/types'
// import type { Player } from '@/types/types'
import { onMounted, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import AppButton from '@/components/ui/AppButton.vue';
import PrepareCard from '@/components/TicTacToe/PrepareCard.vue'


let ws_data = ref<any>({})

const isLoading = ref(false)

watch(ws_data, (newData) => {
  console.log(newData)
})

const store = usePlayerStore()
const route = useRoute()
const sessionId = route.params.id as string

const onPrepareClick = (choose: string) => {
  isLoading.value = !isLoading.value
  const initialMessage: MessageWS = {
    user: store.player_id,
    action: 'prepared',
  }
  useWS(sessionId, initialMessage, ws_data)
  const chooseMessage: MessageWS = {
    user: store.player_id,
    action: "choose",
    type: choose
  }
  useWS(sessionId, chooseMessage, ws_data)
}

onMounted(() => {
  const initialMessage: MessageWS = {
    user: store.player_id,
    action: 'prepared',
  }
  useWS(sessionId, initialMessage, ws_data)
})

</script>
<template>
  <div>
    TicTacToe {{ $route.params.id }}
    <main class="flex justify-center items-center min-h-screen">
      <div v-if="ws_data.status === 'ready'">
        <PrepareCard @prepare-click="onPrepareClick" :markersData="ws_data.markers" :isLoading="isLoading"/>
      </div>
      <Field
        v-else-if="ws_data.status === 'playing'"
        :data="ws_data.field"
      />
      <WaitingForm v-else
        :session_id="sessionId"
        />
    </main>
  </div>
</template>

<style scoped>

</style>
