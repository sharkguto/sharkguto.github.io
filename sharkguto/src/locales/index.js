import messages from "@intlify/unplugin-vue-i18n/messages";
import { createI18n } from "vue-i18n";

// no caso de nao ter default precisa colocar {}, import { i18n } from "@/locales";
export const i18n = createI18n({
    legacy: false,
    globalInjection: true,
    locale: "en-us",
    fallbackLocale: "en-us",
    availableLocales: ["en-us", "pt-br"],
    messages: messages,
});

// export default i18n;
// quando tem default export vc importa ele sem {}, import i18n from "@/locales";
