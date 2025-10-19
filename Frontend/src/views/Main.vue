<!-- Это будет главный экран с где можно и зарегаться и создать лобби и прочее -->
<template>
  <div>
  <input type="text" placeholder="ID" class="bg-white border-2 mx-50 mt-5" v-model="playerId"></input>
  <AppButton message="Создать сессию" @click="onCreateSession"></AppButton>
  <div class="p-20 grid grid-cols-3 gap-10">

    <div v-if="isLoading" class="p-4">
      Загрузка сессий...
    </div>

    <div v-for="session in sessions" :key="session.session_id">
      <CardSession :status="session.status" :id="session.session_id" :players="session.players" @click="onSessionOpen(session.session_id)"
      class="
      duration-150
      hover:scale-105
      hover:cursor-pointer"
      />
    </div>

  </div>
  </div>
</template>

<script setup lang="ts">
import { useApi, useWS } from '@/composables';
import { ref, onMounted } from 'vue';
import { BackendURL, WebSocketURL, type Session } from '@/types/types';
import CardSession from '@/components/ui/CardSession.vue';
import { useRouter } from 'vue-router';
import AppButton from '@/components/ui/AppButton.vue';

const sessions = ref<Session[]>([]);
const isLoading = ref(true);
const playerId = ref('')
const router = useRouter()

const onCreateSession = async () => {
  try {
    const endpoint = `session/create_session/?player_id=${playerId.value}`;
    const response = await useApi.post(endpoint, {});
    const newSession: Session = response.data;
    router.push(`/session/${newSession.session_id}`);
  } catch (error) {
    console.error("Ошибка при создании сессии:", error);
  }
};

const onSessionOpen = async (session_id: string) => {
  try {
    const endpoint = playerId.value
      ? `session/join_session/${session_id}?player_id=${playerId.value}`
      : `session/join_session/${session_id}`;
    await useApi.patch(endpoint, null);
    router.push(`/session/${session_id}`);
  } catch (error) {
    console.error("Ошибка при присоединении к сессии:", error);
    alert("Не удалось присоединиться к сессии. Возможно, она уже заполнена.");
  }
};

onMounted(async () => {
  try {
    const result = await useApi.get('session/sessions');
    sessions.value = result.data;
  } catch (error) {
    console.error("Ошибка при загрузке сессий:", error);
  } finally {
    isLoading.value = false;
  }
});
</script>
