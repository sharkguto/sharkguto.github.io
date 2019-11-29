import Vue from 'vue';
import CountryFlag from 'vue-country-flag';
import BootstrapVue from 'bootstrap-vue';
import VueMeta from 'vue-meta';

import router from './router';
import store from './store';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import i18n from './translate';

import App from './App.vue';

Vue.use(VueMeta, {
  refreshOnceOnNavigation: true,
});

Vue.component('country-flag', CountryFlag);
Vue.use(i18n);

Vue.use(BootstrapVue);


Vue.config.productionTip = false;

// Vue.config.configureWebpack = {
//   optimization: {
//     splitChunks: false,
//   },
//   css: {
//     extract: false,
//   },
// };


new Vue({
  router,
  store,
  i18n,
  render: h => h(App),
}).$mount('#app');
