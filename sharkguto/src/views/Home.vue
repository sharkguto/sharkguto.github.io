<template>
  <div>
    <img alt="GMF-tech logo" class="img-fluid" src="../assets/logo.png">
    <HelloWorld :msg="msg"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '../components/HelloWorld.vue';
import store from '../store';


export default {
  name: 'home',
  data() {
    return {
      msg: `Welcome to Your Vue.js App ${store.getters.counter}`,
    };
  },
  components: {
    HelloWorld,
  },
};
</script>
