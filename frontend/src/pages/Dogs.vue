<template>
  <section>
    <select v-model="selected">
      <option v-for="dog in dogs" :value="dog">{{ dog.name }}</option>
    </select>
    <Dog :dog="selected"></Dog>
  </section>
</template>

<script setup>
import { ref, onMounted } from "vue";
import Dog from "../components/Dog.vue";

const dogs = ref();

const selected = ref(null);

onMounted(async () => {
  try {
    const response = await fetch("http://127.0.0.1:8000/api/dogs/", {
      method: "get",
      mode: "cors",
    });
    console.log(response);
    if (response.ok) {
      dogs.value = await response.json();
    } else {
      console.error("Failed to fetch data");
    }
  } catch (error) {
    console.error("Error fetching data:", error);
  }
});
</script>
