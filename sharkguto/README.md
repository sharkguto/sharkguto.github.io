# sharkguto

## Project setup

```
npm install
```

### Compiles and hot-reloads for development

```
npm run serve
```

### Compiles and minifies for production

```
npm run build
```

### Lints and fixes files

```
npm run lint
```

### Customize configuration

See [Configuration Reference](https://cli.vuejs.org/config/).

## install

```bash
sudo npm i -g @vue/cli --scripts-prepend-node-path
vue create project
npm install axios --save
```

## hard reset

```bash
git reset --hard 8a1625fc98f3ed0df9e64cd3917499d39b6ad0a4
git push --force origin master
```

## vue tips

for biding

```vue
<p :data="variable1">{{variable1}}</>
```

```vue
v-model v-on:click or @click @submit.prevent="event++" :class="[isActive ?
'active' : 'notActive']"
```

```vue
computed: {
    funcname(){return "a"}
}
data: {
    isActive: "ok"
}
watch: {
    isActive: function(args){
        console.log(` ok ok ${args}`);
        }
}

```

```vue
Vue.component('componentname', {
    template: `<h1>testing</h1>`
})
```
