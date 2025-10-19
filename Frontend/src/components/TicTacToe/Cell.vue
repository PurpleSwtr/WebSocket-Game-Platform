<script setup lang="js">
const props = defineProps({
  // cell_id наверное всё-таки рудимент тоже, потому что для других игр id будет неявно.
  cell_id: Number,
  row: Number,
  col: Number,
  symbol: String,
})
</script>

<template>
  <div
    class="bg-gray-300 w-8 h-8 rounded-xl m-1 hover:bg-gray-400 transition-colors duration-100 hover:cursor-pointer text-center p-1"
    @click="$emit('cellClick', row, col)"
  >
    <p>{{ symbol }}</p>
  </div>
</template>

<style scoped>
</style>
