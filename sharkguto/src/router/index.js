import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Login from '../views/Login.vue';
import store from '../store';

Vue.use(VueRouter);

function requireAuth(to, from, next) {
  if (!store.getters.isLogged) {
    next({
      path: '/login',
      query: { redirect: to.name },
    });
  } else {
    next();
  }
}

function logoff(to, from, next) {
  if (store.getters.isLogged) {
    store.commit('logoff');
    next({ path: '/login' });
  } else {
    next();
  }
}


const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/logoff',
    name: 'logoff',
    beforeEnter: logoff,
  },
  {
    path: '/about',
    name: 'about',
    beforeEnter: requireAuth,
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
  },
  {
    path: '/products',
    name: 'products',
    beforeEnter: requireAuth,
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Products.vue'),
  },
  {
    path: '/login',
    name: 'login',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: Login,
    beforeEnter: logoff,
    // component: () => import(/* webpackChunkName: "about" */ '../views/Login.vue'),
  },
];

const router = new VueRouter({
  routes,
  mode: 'history',
});

export default router;
