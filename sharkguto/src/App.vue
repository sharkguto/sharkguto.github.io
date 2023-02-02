<script setup>
import { ref } from "vue";
import i18n from "@/locales";

const languages = [
  { flag: "us", language: "en-us", title: "English" },
  { flag: "br", language: "pt-br", title: "Portuguese" },
];

// ref para valores primitivos

// reactive para objetos json
const accname = ref("gmf-tech");

function changeLocale (lang_locale) {
  //store.commit('setLanguage', locale);

  console.log(lang_locale);
  i18n.global.locale.value = lang_locale;
  //t.locale = lang_locale;
}
</script>

<template>
  <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link :to="{ name: 'news', params: { account: accname } }">
      {{ accname }}</router-link>
    <input v-model="accname" placeholder="edit me" />
    <router-link to="/contact">Contact</router-link>
    <div class="col-4">
      <div class="row">
        <button class="btn col-4" v-for="entry in languages" :key="entry.title" @click="changeLocale(entry.language)">
          <country-flag :country="entry.flag" v-bind:squared="false" size="small" />
          {{ $t (entry.title) }}
        </button>
      </div>
    </div>
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
