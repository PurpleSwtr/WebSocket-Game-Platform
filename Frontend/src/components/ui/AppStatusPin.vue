<template>
  <AppIcon icon_name="miniuser"
  class="scale-90 inline text-gray-700"
  />
  <span class="inline p-1 text-gray-700 font-semibold">{{cnt_players}} / 2</span>
  <div class="absolute right-6 top-6">
    <div class="px-3 h-max w-max bg-amber-300 rounded-xl">
       <span>
         {{status}}
       </span>
     </div>
    </div>
    <div class="border-t border-gray-200 my-2"></div>
</template>

<script setup lang="ts">
import AppIcon from './AppIcon.vue';

defineProps({
  status: String,
  cnt_players: Number,
  required: Number,
});
</script>
