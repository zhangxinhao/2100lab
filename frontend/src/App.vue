<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
    }
  }
}
</script>

<style>
body {
  margin: 0px;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
@media screen and (max-width: 500px) {
    .el-carousel {
      max-width: 1200px;
      max-height: 120px;
    }
    .el-carousel__container {
      max-width: 1200px;
      max-height: 120px;
    }
  }
.el-carousel__container {
  height: 350px;
}
</style>
