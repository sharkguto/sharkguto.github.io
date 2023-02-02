import { createApp } from "vue";
import "@/assets/scss/style.scss";
import Oruga from "@oruga-ui/oruga-next";
import "@oruga-ui/oruga-next/dist/oruga.css";
import CountryFlag from "vue-country-flag-next";

import router from "@/router";

import App from "@/App.vue";

import i18n from "@/locales";

const app = createApp(App);
app.use(Oruga);
app.use(router);
app.use(i18n);

app.component("country-flag", CountryFlag);

app.mount("#app");
