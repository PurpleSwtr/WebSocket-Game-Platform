<script setup lang="ts">
import Cell from '@/components/Cell.vue'
import Field from '@/components/TicTacToe/Field.vue'
</script>
<template>
  <main class="flex justify-center items-center min-h-screen">
    <Field />
  </main>
</template>

<style scoped>
.text {
  background-color: green;
  color: white;
}
</style>
