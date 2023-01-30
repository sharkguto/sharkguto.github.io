<script setup>
import { ref, reactive } from 'vue'


// ref para valores primitivos
// reactive para objetos json
const accname = ref('gmf-tech');


</script>

<template>
  <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link :to="{ name: 'news', params: { account: accname } }"> {{ accname }}</router-link>
    <input v-model="accname" placeholder="edit me" />
    <router-link to="/contact">Contact</router-link>
  </div>
  <router-view />
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
}

.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}

.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
