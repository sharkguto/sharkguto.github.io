import { createWebHistory, createRouter } from "vue-router";

import Contact from "@/components/contact/Contact.vue";
import Home from "@/components/home/Home.vue";
import News from "@/components/news/News.vue";

const routes = [
    {
        path: "/",
        name: "home",
        component: Home,
    },
    {
        path: "/contact",
        name: "contact",
        component: Contact,
    },
    {
        path: "/:account",
        name: "news",
        component: News,
    },
];

export const router = createRouter({
    history: createWebHistory(),
    routes,
});
