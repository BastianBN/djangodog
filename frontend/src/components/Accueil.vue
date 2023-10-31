<script setup>
import { ref } from "vue";

defineProps({
  msg: String,
});
</script>

<template>
  <div class="grid h-screen place-items-center">
    <img src="../assets/doge.png" class="w-5/12" />
    <h1 class="text-4xl">
      This is the dog viewer
      <h1>Click <router-link to="/dogs"> here </router-link> to access dogs</h1>
    </h1>
  </div>
</template>
k
<style scoped></style>
