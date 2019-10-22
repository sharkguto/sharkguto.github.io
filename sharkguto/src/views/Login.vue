<template>
  <div class="row">
    <img alt="GMF-tech logo" class="img-fluid" src="../assets/logo.png">
    <LoginForm :msg="msg"/>
  </div>
</template>

<script>
// @ is an alias to /src

import LoginForm from '../components/LoginForm.vue';

export default {
  name: 'home',
  data() {
    return {
      msg: 'Welcome to Your Vue.js App',
    };
  },
  components: {
    LoginForm,
  },
};
</script>
