import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    count: 0,
    isLogged: false,
  },
  mutations: {
    incrementCounter(state, payload) {
      state.count += payload;
    },
    login(state, payload) {
      state.isLogged = payload;
    },
  },
  getters: {
    isLogged: state => state.isLogged,
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
