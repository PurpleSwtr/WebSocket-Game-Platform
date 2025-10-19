<!-- Это будет главный экран с где можно и зарегаться и создать лобби и прочее -->
<template>
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
</template>

<script setup lang="ts">
import { useApi, useWS } from '@/composables';
import { ref, onMounted } from 'vue';
import { BackendURL, WebSocketURL, type Session } from '@/types/types';
import CardSession from '@/components/ui/CardSession.vue';
import { useRouter } from 'vue-router';

const sessions = ref<Session[]>([]);
const isLoading = ref(true);
// Это была затычка, нужно ещё подумаь над тем как именно хранить пользователя
// const player = "3fa85f64-5717-4562-b3fc-2c963f66afa7"
const router = useRouter()

const onSessionOpen = async (session_id: string) => {
  try {
    // const endpoint = `session/join_session/${session_id}?player_id=${player}`;
    const endpoint = `session/join_session/${session_id}`;
    await useApi.patch(endpoint, null);
    router.push(`/session/${session_id}`);
  } catch (error) {
    console.error(error);
  }
};

onMounted(async () => {
  try {
    const result = await useApi.get('session/sessions');
    sessions.value = result.data;
    console.log(sessions.value)
  } catch (error) {
    console.error("Ошибка при загрузке сессий:", error);
  } finally {
    isLoading.value = false;
  }
});
</script>
