<template>
  <div id="app" class="container-fluid">
    <div id="nav">
      <div class="row">
        <div class="col-8">
          <router-link to="/">{{$t("Home")}}</router-link>
          <router-link v-if="$store.getters.isLogged" to="/about">{{$t("About")}}</router-link>
          <router-link v-if="$store.getters.isLogged" to="/products">
            {{$t("Products")}}
          </router-link>
          <router-link v-if="!$store.getters.isLogged" to="/login">{{$t("Login")}}</router-link>
          <router-link v-if="$store.getters.isLogged" to="/logoff">{{$t("Logoff")}}</router-link>
        </div>
        <div class="col-4">
          <div class="row">
            <button class="btn col-4" v-for="entry in languages"
          :key="entry.title" @click="changeLocale(entry.language)">
                <country-flag :country="entry.flag" v-bind:squared=false size='small'/>
                 {{ $t(entry.title) }}
            </button>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <router-view/>
      </div>
    </div>
  </div>
</template>

<script>

import store from './store';
import i18n from './translate';

export default {
  name: 'app',
  metaInfo: {
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width,initial-scale=1.0' },
    ],
    title: 'GMF-TECH',
    titleTemplate: '%s - ship',
    htmlAttrs: {
      lang: store.getters.locale,
      amp: true,
    },
  },
  data() {
    return {
      languages: [
        { flag: 'us', language: 'en', title: 'English' },
        { flag: 'br', language: 'br', title: 'Portuguese' },
      ],
    };
  },
  methods: {
    changeLocale(locale) {
      store.commit('setLanguage', locale);
      i18n.locale = locale;
    },
  },
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
