<script setup lang="ts">
import { ref, onMounted } from 'vue';
import LoadingCircle from './LoadingCircle.vue';

const props = defineProps<{
  session_id: string
}>()

const link = ref('')

onMounted(() => {
  if (props.session_id)
  {
    const host = window.location.host;
    const protocol = window.location.protocol;
    link.value =`${protocol}//${host}/session/${props.session_id}`
  }
})

</script>
<template>
  <div class="h-70 bg-white rounded-3xl flex flex-col items-center justify-center gap-4 px-8 py-6 scale-130 shadow-xl">
    <div class="flex items-center gap-5">
      <h1 class="text-2xl">
        Ожидание игроков
      </h1>
      <div class="animate-bounce">
        <LoadingCircle class="scale-150"/>
      </div>
    </div>

    <div class="text-center">
      <div>Ссылка на подключение:</div>
      <input
        type="text"
        :value="link"
        readonly
        class=" text-xs text-center border-1 rounded-md px-2 py-1 mt-2 w-120 border-blue-600 outline-blue-600"
      />
    </div>
  </div>
</template>
