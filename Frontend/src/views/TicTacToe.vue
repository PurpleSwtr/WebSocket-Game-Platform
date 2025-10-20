<script setup lang="ts">
import Field from '@/components/TicTacToe/Field.vue'
import WaitingForm from '@/components/ui/WaitingForm.vue'
import { usePlayerStore } from '@/stores/playerStore'
import type { MessageWS } from '@/types/types'
import { onMounted, onUnmounted, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import PrepareCard from '@/components/TicTacToe/PrepareCard.vue'
import { disconnectWS, initWS, sendWS } from '@/composables/useWebsocket'
import { useApi } from '@/composables'


let ws_data = ref<any>({})

const isLoading = ref(false)

watch(ws_data, (newData) => {
  console.log(newData)
})

const store = usePlayerStore()
const route = useRoute()
const sessionId = route.params.id as string

const onFieldClick = (fieldClickData: { row: number, col: number }) => {
  console.log([fieldClickData.row, fieldClickData.col])
  const moveMessage: MessageWS = {
    user: store.player_id,
    action: 'move',
    row: fieldClickData.row,
    col: fieldClickData.col,
  }
  sendWS(moveMessage)
}

const onPrepareClick = (prepareData: { choose: string }) => {
  isLoading.value = !isLoading.value

  const chooseMessage: MessageWS = {
    user: store.player_id,
    action: "choose",
    type: prepareData.choose
  }
  sendWS(chooseMessage)

  const preparedMessage: MessageWS = {
    user: store.player_id,
    action: 'prepared',
  }
  sendWS(preparedMessage)
}

onMounted(async () => {
  if (!store.player_id) {
    try {
      const response = await useApi.patch(`session/join_session/${sessionId}`, null);

      const players = response.data.players;
      const playerIds = Object.keys(players);

      const myNewId = playerIds[playerIds.length - 1];

      if (myNewId) {
        store.addPlayerId(myNewId);
      } else {
        throw new Error("Не удалось получить ID игрока от сервера.");
      }

    } catch (error) {
      console.error("Ошибка при присоединении гостя:", error);
      alert("Не удалось присоединиться к сессии. Возможно, она уже заполнена.");
      return;
    }
  }
  initWS(sessionId, ws_data);
});

onUnmounted(() => {
  disconnectWS();
});

</script>
<template>
  <div>
    TicTacToe {{ $route.params.id }}
    <main class="flex justify-center items-center min-h-screen">
      <div v-if="ws_data.status === 'ready' || ws_data.status === 'ready_to_start'">
        <PrepareCard @prepare-click="onPrepareClick" :markersData="ws_data.markers" :isLoading="isLoading"/>
      </div>
      <Field
        v-else-if="ws_data.status === 'playing'"
        :field_data="ws_data.field"
        :current_turn="ws_data.players[ws_data.current_turn].name"
        @field-click="onFieldClick"
      />
      <WaitingForm v-else
        :session_id="sessionId"
        />
    </main>
  </div>
</template>

<style scoped>

</style>
