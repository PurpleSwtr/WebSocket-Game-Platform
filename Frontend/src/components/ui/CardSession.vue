<template>
 <div class="relative overflow-hidden w-80 h-60 bg-white rounded-4xl shadow-xl p-6">
  <div class="z-10">
    <AppStatusPin :status="status"/>
      <h1 class="text-md text-gray-700 font-semibold pt-2">Комната:</h1>
      <h1 class="text-xs text-gray-700">{{id}}</h1>
      <h1 class="text-md text-gray-700 font-semibold pt-2 flex flex-nowrap">
        <p>Игроки:</p>
        <p class="px-2 z-20">
          {{players_names}}
        </p>
      </h1>
  </div>
  <AppIcon icon_name="cross" class="absolute bottom-4 right-4 z-1 text-red-300 scale-500 rotate-13"/>
  <AppIcon icon_name="circle" class="absolute bottom-2 left-4 z-1 text-blue-200 scale-700 rotate-13 "/>

  </div>
</template>

<script setup lang="ts">
import { onMounted, onUpdated, ref } from 'vue';
import AppIcon from './AppIcon.vue';
import type { Player } from '@/types/types';
import AppStatusPin from './AppStatusPin.vue';

interface Props {
  id: string;
  status: string;
  players: Record<string, Player> | Player[];
}

const props = defineProps<Props>();

const players_names = ref<string>('');

onMounted(() => {
  if (props.players) {
    if (Array.isArray(props.players)) {
      players_names.value = props.players.map(player => player.name).join(', ');
    } else {
      players_names.value = Object.values(props.players).map(player => player.name).join(', ');
    }
  }
});
</script>
