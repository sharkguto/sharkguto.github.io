import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';

// Vue.config.productionTip = true;
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
  render: h => h(App),
}).$mount('#app');
