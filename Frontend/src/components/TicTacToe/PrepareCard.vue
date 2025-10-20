<template>
  <div class="flex items-center justify-center relative w-220 h-80 bg-white shadow-2xl rounded-3xl">
    <nav class="flex items-center justify-center gap-5 w-60 h-40">
      <ul class="flex gap-5">
        <li v-for="(icon, key) in icons_map" :key="key">
          <div
            class="w-24 h-24 border-gray-400 cursor-pointer rounded-3xl flex justify-center items-center duration-200 hover:scale-110 hover:-translate-y-3 transition-all"
            :class="[
              key === selectedIconKey
                ? `${icon.color} text-white`
                : 'bg-stone-100 text-gray-300',
              icon.hoverColor,
              'hover:text-white'
            ]"
            @click="onChooseType(key, icon.symbol)"
          >
            <AppIcon
              :icon_name="icon.icon"
              class="scale-250"
            />
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
import { icons_map, type IconKey } from '@/types/types';

const emit = defineEmits(['prepareClick'])

const selectedIconKey = ref<IconKey | null>(null);

const onChooseType = (key: IconKey, symbol: string) => {
  selectedIconKey.value = key;
}

const onPrepareClick = () => {
  if (selectedIconKey.value) {
    const selectedSymbol = icons_map.value[selectedIconKey.value].symbol;
    emit('prepareClick', {
      choose: selectedSymbol,
    });
  } else {
    alert('Пожалуйста, выберите иконку');
  }
}


const props = defineProps<{
  isLoading: boolean;
  markersData: any;
}>();
</script>
