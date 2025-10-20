<script setup lang="ts">
import { onMounted } from 'vue';

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

</script>

<template>
  <div
    class="bg-gray-300 w-8 h-8 rounded-xl m-1 hover:bg-gray-400 transition-colors duration-100 hover:cursor-pointer text-center p-1"
    @click="onCellClick"
  >
    <p>{{ symbol }}</p>
  </div>
</template>

<style scoped>
</style>
