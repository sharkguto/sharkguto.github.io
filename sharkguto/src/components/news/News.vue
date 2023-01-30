<script setup>
import { ref,reactive, onUpdated } from 'vue'
import {useRoute} from 'vue-router'

let route = useRoute();
console.log(route);
let account = ref(route.params.account);



onUpdated(() => {
    account = route.params.account;
})

</script>

<template>
    <div>News for {{account}}</div>
</template>