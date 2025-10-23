<script setup lang="ts">
import GameCard from './GameCard.vue';

const games_data = {
  "tictactoe": {
    title: "Крестики-нолики",
    icon: "tictactoe",
    subtitle: "Попробуйте свою логику в деле!",
  },
  "ships": {
    title: "Морской бой",
    icon: "ships",
    subtitle: "Потопите корабли противника!",
  },
  "quiz": {
    title: "Викторина",
    icon: "quiz",
    subtitle: "Проверьте свои знания!",
  },
}

</script>

<template>
  <div class="grid grid-cols-3 gap-10">
    <GameCard
      v-for="(game, key) in games_data"
      :key="key"
      :title="game.title"
      :icon="game.icon"
      :subtitle="game.subtitle"
    ></GameCard>
  </div>
</template>
