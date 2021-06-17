<template>
  <div id="app">
    <appnav/>
    
    
    <!-- <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
    <router-link to="/contact">contact</router-link>
    <router-link to="/shop">shop</router-link>
    <router-link to="/shops">shops</router-link>
    <router-link to="/login">login</router-link> -->
    <router-view/>
  <appfoot/>
  </div>
  
</template>


<script>
import appnav from './components/appnav.vue'

import appfoot from './components/appfoot.vue'

export default {
    name:'app',
    components:{
        appnav,
        appfoot
    }
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

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
