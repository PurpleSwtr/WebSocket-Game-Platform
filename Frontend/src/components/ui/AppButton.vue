<template>
    <button :disabled="props.statusLoading"
    class="cursor-pointer
    bg-green-600
    hover:bg-green-700
    transition-colors
    rounded-full
    px-5 py-2
    text-white
    font-semibold
    fade
    disabled:bg-amber-500
    disabled:cursor-default
    shadow-md">
    <span v-if="!props.statusLoading">{{props.message}}</span>
    <span v-else class="inline-flex items-center gap-x-2">
        Загрузка
        <LoadingCircle class="text-base " />
    </span>
    </button>

</template>

<script setup lang="ts">
    import LoadingCircle from './LoadingCircle.vue';

    const props = defineProps<{
        message: string
        statusLoading?: boolean
    }>()

</script>

<style scoped>

</style>
