import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import { fileURLToPath } from "url";
import { resolve, dirname } from "path";
import VueI18nPlugin from "@intlify/unplugin-vue-i18n/vite";
// https://vitejs.dev/config/
export default defineConfig({
    plugins: [
        vue(),
        VueI18nPlugin({
            include: resolve(
                dirname(fileURLToPath(import.meta.url)),
                "./src/locales/**"
            ),
        }),
    ],
    resolve: {
        alias: {
            "@": fileURLToPath(new URL("./src", import.meta.url)),
        },
    },
    // css: {
    //     preprocessorOptions: {
    //         scss: {
    //             additionalData: `
    //               @import 'bulma/sass/utilities/_all';
    //               @import 'bulma/bulma';
    //             `,
    //         },
    //     },
    // },
    server: {
        port: 3000,
    },
    build: {
        brotliSize: false, // unsupported in StackBlitz
    },
});
