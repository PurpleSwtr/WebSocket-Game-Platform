<script setup lang="ts">
import AppNavBar from '@/components/MainView/AppNavBar.vue'
import FlagmanSection from '@/components/MainView/FlagmanSection.vue';
import TittleSection from '@/components/MainView/TittleSection.vue'
</script>

<template>
  <div class="flex min-h-screen bg-gray-100 pt-6">
    <div class="items-center container mx-auto px-4">
      <AppNavBar></AppNavBar>
      <TittleSection class="mt-6"></TittleSection>
      <FlagmanSection></FlagmanSection>
    </div>
  </div>
</template>

<style scoped></style>
