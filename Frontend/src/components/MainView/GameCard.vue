<script setup lang="ts">
defineProps<{
  icon: string
  title: string
  subtitle: string
  locked?: false
}>();

import AppButton from '../ui/AppButton.vue';
import AppIcon from '../ui/AppIcon.vue';
</script>

<template>
  <div class="h-60 w-80 bg-white shadow-lg shadow-gray-300 rounded-3xl flex flex-col justify-center items-center text-center">
    <div class="w-24 h-24 flex justify-center items-center bg-amber-300 rounded-3xl text-gray-700">
      <AppIcon :icon_name="icon"></AppIcon>
    </div>
    <p class="font-bold pt-2 text-gray-700">{{title}}</p>
    <p class="font-thin text-stone-400">{{subtitle}}</p>
    <AppButton message="Подробнее" class="scale-75 mt-5"></AppButton>
  </div>
</template>

<style scoped></style>
