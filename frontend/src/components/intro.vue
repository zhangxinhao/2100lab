<template>
  <div id="body">
    <div style="text-align: center; margin:0px; ">
      <img alt="" :src="picture" width="700" height="300"/>
    </div>
    <div id="page">
      <div id="class">课程 {{ title }}</div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: "我们爱科学",
      picture: require('../assets/class2.jpg')
    }
  },
  methods: {
    handleChange(value) {
      console.log(value)
    }
  }
}
</script>
<style>
</style>
