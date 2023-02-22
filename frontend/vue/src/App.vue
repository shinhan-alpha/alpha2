<template>
  <status-bar></status-bar>
    <router-view style="margin-top: 38px;"/>
    <tab-bar></tab-bar>
</template>

<script>
import StatusBar from './components/StatusBar.vue'
import TabBar from './components/TabBar.vue'

export default {
  components: {TabBar, StatusBar}
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
