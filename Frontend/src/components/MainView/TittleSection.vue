<script setup lang="ts">
import AppButton from '../ui/AppButton.vue';

</script>

<template>
  <div class="relative flex flex-col items-center justify-center py-30 space-y-8">
    <h1 class="text-5xl font-semibold tracking-normal text-rose-400">Let's play all over the world!</h1>
    <AppButton class="bottom-15 scale-120 absolute" message="Быстрый старт" loading_message="Загрузка"/>
  </div>
</template>

<style scoped></style>
