<script setup lang="js">
import { ref } from 'vue'

const props = defineProps({
  cell_id: Number,
  symbol: String,
})

// const msg = ref('idle')

// const states = {
//   idle: '',
//   miss: '0',
//   hit: 'x',
// }

// const onClick = () => {
//   msg.value = props.symbol
// }
</script>

<template>
  <div
    class="bg-gray-300 w-8 h-8 rounded-xl m-1 hover:bg-gray-400 transition-colors duration-100 hover:cursor-pointer text-center p-1"
    @click="$emit('cellClick', cell_id)"
  >
    <p>{{ symbol }}</p>
  </div>
</template>

<style scoped>
/* .idle {
  background-color: gray;
  width: 240px;
  height: 240px;
} */
</style>
