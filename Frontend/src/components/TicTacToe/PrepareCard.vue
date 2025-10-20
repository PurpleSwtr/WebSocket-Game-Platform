<template>
  <div class="flex items-center justify-center relative overflow-hidden w-120 h-80 bg-white shadow-2xl rounded-3xl">
    <nav class=" flex items-center justify-center gap-5 w-60 h-40">
      <ul class="flex gap-5">
        <li v-for="icon in icons_map">
          <div class="w-24 h-24 border-2 border-gray-400 cursor-pointer rounded-3xl flex justify-center items-center bg-gray-50 duration-150 hover:scale-110 hover:-translate-y-3"
          :class="(icon.border)">
            <AppIcon :icon_name="icon.icon"
            class="scale-250"
            :class="(icon.color)"
            @click="onChooseType(icon.symbol)"/>
          </div>
        </li>
      </ul>
    </nav>
    <AppButton
    class="absolute bottom-10 right-10"
    message="Готов"
    @click="onPrepareClick"
    :statusLoading="props.isLoading"
    loading_massage="Ждём остальных игроков"
    />
  </div>
</template>

<!-- Огонь - красный R
Квадрат - оранжевый O
Молния - жёлтый Y
Крест - зелёный G
Капля - голубой L
Круг - синий B
Треугольник - фиолетовый P -->

<script setup lang="ts">
import { ref } from 'vue';
import AppButton from '@/components/ui/AppButton.vue';
import AppIcon from '../ui/AppIcon.vue';
const emit = defineEmits(['prepareClick'])

const choose = ref('')

const onChooseType = (icon: string) => {
  choose.value = icon
  console.log(choose.value)
}

const onPrepareClick = () => {
  emit('prepareClick', {
    choose: choose.value,
  })
}

const icons_map = ref({
  "cross": {
    "icon": "cross",
    "symbol": "X",
    "color": "text-blue-200",
    "border": "border-blue-200"
  },
  "circle": {
    "icon": "circle",
    "symbol": "O",
    "color": "text-red-300",
    "border": "border-red-300"
  },
})

const props = defineProps<{
  isLoading: boolean
  markersData: any,
}>()
</script>
