import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate';

Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [createPersistedState({ paths: ['count', 'isLogged'] })],
  state: {
    count: 0,
    isLogged: false,
  },
  mutations: {
    incrementCounter(state, payload) {
      state.count += payload;
    },
    countPlus(state) {
      state.count += 1;
    },
    countReset(state) {
      state.count = 0;
    },
    login(state) {
      state.isLogged = true;
    },
    logoff(state) {
      state.isLogged = false;
    },
  },
  getters: {
    isLogged: state => state.isLogged,
    counter: state => state.count,
  },
  actions: {
    incrementAction(context, payload) {
      context.commit('incrementCounter', payload);
    },
    loginAction(context, payload) {
      context.commit('login', payload);
    },

  },
  modules: {
  },
});
