<!-- Тут нужно создать сессию, где будут методы обеспечивающие для всех игр логику подключения и предоставлять инструменты для взаимодействия -->
<script setup lang="ts">
import router from '@/router';
import TicTacToe from '@views/TicTacToe.vue';
</script>

<template>
  TicTacToe {{ $route.params.id }}
</template>
