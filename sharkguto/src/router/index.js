import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Login from '../views/Login.vue';
import store from '../store';
import About from '../views/About.vue';
import Products from '../views/Products.vue';

Vue.use(VueRouter);

function requireAuth(to, from, next) {
  if (!store.getters.isLogged) {
    next({
      path: '/login',
      query: { redirect: to.name },
    });
  } else {
    store.commit('countPlus');
    next();
  }
}

function logoff(to, from, next) {
  if (store.getters.isLogged) {
    store.commit('logoff');
    store.commit('countReset');
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
    beforeEnter: (to, from, next) => { store.commit('countPlus'); next(); },

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
    // component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
    // component: () => import('../views/About.vue'), // for chunk
    component: About,
  },
  {
    path: '/products',
    name: 'products',
    beforeEnter: requireAuth,
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    // component: () => import(/* webpackChunkName: "products" */ '../views/Products.vue'),
    // component: () => import('../views/Products.vue'),
    component: Products,
  },
  {
    path: '/login',
    name: 'login',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: Login,
    beforeEnter: logoff,
  },
];

const router = new VueRouter({
  routes,
  mode: 'history',
});

export default router;
