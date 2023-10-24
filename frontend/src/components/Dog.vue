<template>
  <div v-if="props.dog" class="grid grid-flow-col rounded-2xl bg-white p-4 text-black w-5/6">
    <div v-for="(value, name) in props.dog" :key="name" class="flex flex-col">
      <div v-if="name === 'breed'" v-for="(note, charac) in props.dog.breed">
        <p>{{ charac }}</p>
        <p>{{ note }}</p>
      </div>
      <div v-else>
        <p class = "text-xl">{{ name[0].toUpperCase() + name.slice(1) }}</p> <p class="text-lg"> {{ value }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  dog: { type: Object },
});
</script>
