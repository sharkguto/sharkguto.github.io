import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import { fileURLToPath } from "url";
// https://vitejs.dev/config/
export default defineConfig({
    plugins: [vue()],
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
