

<template>
  <div class="row">
    <h1 v-if="!$store.getters.isLogged">{{ $store.getters.isLogged }}</h1>
    <h1 v-if="$store.getters.isLogged">{{ $t('welcomeMsg') }} {{ msg }}</h1>
  </div>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>


<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String,
  },
};
</script>
