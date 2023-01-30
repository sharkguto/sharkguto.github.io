<script setup>
import { ref, onUpdated , onMounted} from 'vue'
import {useRoute} from 'vue-router'

let route = useRoute();
console.log(route);
let account = ref(route.params.account);

onMounted(() => {
    console.log("onMounted news");
    account.value = route.params.account;
})

onUpdated(() => {
    console.log("onUpdated news");
    account.value = route.params.account;
})

</script>

<template>
    <div>News for {{account}}</div>
</template>