import Vue from 'vue';
import VueI18n from 'vue-i18n';
import store from '../store';

Vue.use(VueI18n);

const messages = {
  en: {
    welcomeMsg: 'Welcome to Your Vue.js App',
    English: 'English',
    Portuguese: 'Portuguese',
    Home: 'Home',
    About: 'About',
    Login: 'Login',
    Logoff: 'Logoff',
    Products: 'Products',
  },
  br: {
    welcomeMsg: 'Bem vindo ao Vue.js',
    English: 'Inglês',
    Portuguese: 'Portugues',
    Home: 'Principal',
    About: 'Sobre',
    Login: 'Autenticar',
    Logoff: 'Sair',
    Products: 'Produtos',
  },
};

const i18n = new VueI18n({
  locale: store.getters.locale ? store.getters.locale : 'br', // set locale
  fallbackLocale: 'en', // set fallback locale
  messages, // set locale messages
});

export default i18n;
