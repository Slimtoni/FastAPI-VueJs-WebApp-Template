<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <PostRequest></PostRequest>
  </div>
</template>

<script>
import PostRequest from "@/components/PostRequest";
export default {
  name: 'App',
  components: {
    PostRequest
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
  margin-top: 60px;
}
</style>
