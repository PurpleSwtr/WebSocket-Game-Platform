<script setup lang="ts">
import { computed } from 'vue';

const icons = import.meta.glob('@/assets/icons/*.svg', { eager: true });

const props = defineProps({
    icon_name: String,
})

const iconComponent = computed(() => {
    const path = `/src/assets/icons/${props.icon_name}.svg`;
    return icons[path];
});
</script>

<template>
    <component :is="iconComponent"/>
</template>