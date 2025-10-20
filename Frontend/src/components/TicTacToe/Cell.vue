<script setup lang="ts">
import { computed, onMounted } from 'vue';
import AppIcon from '../ui/AppIcon.vue';
import { icons_map } from '@/types/types';

const props = defineProps<{
  cell_id: number
  symbol: string | null
}>()

const emit = defineEmits(['cellClick'])

const onCellClick = () => {
  emit('cellClick', {
    id: props.cell_id
  })
}

const iconDetails = computed(() => {
  if (!props.symbol) {
    return null;
  }
  return Object.values(icons_map.value).find(icon => icon.symbol === props.symbol) || null;
});
</script>

<template>
  <div
    @click="onCellClick"
    :class="[
      'w-8 h-8 rounded-xl m-1 transition-colors duration-100 flex justify-center items-center',
      iconDetails
        ? [iconDetails.color, 'text-white', 'cursor-default']
        : 'bg-gray-200 hover:bg-gray-300 hover:cursor-pointer'
    ]"
  >
    <AppIcon v-if="iconDetails" :icon_name="iconDetails.icon" class="scale-90"/>
  </div>
</template>

<style scoped>
</style>
