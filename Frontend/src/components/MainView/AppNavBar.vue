<script setup lang="ts">
const navLinkClass = 'cursor-pointer transition-all duration-150 hover:text-orange-600'
</script>

<template>
  <header class="h-14 w-full bg-white rounded-full shadow-lg shadow-gray-200">
    <nav class="flex justify-between items-center h-full px-20 text-xl text-gray-600">
      <div class="flex gap-6">
        <a :class="navLinkClass">Главная</a>
        <a :class="navLinkClass">Игры</a>
        <a :class="navLinkClass">О проекте</a>
      </div>
      <div class="flex">
        <a :class="navLinkClass">Войти</a>
      </div>
    </nav>
  </header>
</template>

<style scoped></style>
