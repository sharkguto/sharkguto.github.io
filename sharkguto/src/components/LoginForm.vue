/**
 * @File   : Login.js
 * @Author : Gustavo Freitas (gustavo@gmf-tech.com)
 * @Link   :
 * @Date   : 10/21/2019, 2:20:39 PM
 */

<template>
    <div class="caravela-login">
        <h4>Login</h4>
        <form>
            <label for="email" >E-Mail Address</label>
            <div>
                <input id="email" type="email" v-model="email" required autofocus>
            </div>
            <div>
                <label for="password" >Password</label>
                <div>
                    <input id="password" type="password" v-model="password" required>
                </div>
            </div>
            <div>
                <button type="submit" @click="handleSubmit">
                    Login
                </button>
            </div>
        </form>
    </div>
</template>

<style scoped>
  .caravela-login {
    z-index: 200;
  }
</style>

<script>
import axios from 'axios';
import store from '../store';

export default {
  data() {
    return {
      email: '',
      password: '',
    };
  },
  methods: {
    handleSubmit(e) {
      e.preventDefault();
      if (this.password.length > 0) {
        console.log(this.password.length);
        // const auth = `Basic ${btoa(`${this.username}:${this.password}`)}`;
        axios.post('https://5daf0f29f2946f001481d271.mockapi.io/v1/login',
          {
            auth: {
              username: this.username,
              password: this.password,
            },
          }).then((response) => {
          console.log(`SUCCESS ${response}`);
          if (response.data.success === true) {
            store.state.isLogged = true;
            console.log(store.state.isLogged);
          }
        })
          .catch((error) => {
            console.error(`ERROR ${error.response}`);
          });
      }
    },
  },
};
</script>
