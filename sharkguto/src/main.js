import { createApp } from "vue";
import "@/assets/scss/style.scss";
import Oruga from "@oruga-ui/oruga-next";
import "@oruga-ui/oruga-next/dist/oruga.css";

import router from "@/router";

import App from "@/App.vue";

import i18n from "@/locales";

const app = createApp(App);
app.use(Oruga);
app.use(router);
app.use(i18n);
app.mount("#app");
