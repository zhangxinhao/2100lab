<template>
  <div id="body">
    <div style="text-align: center; margin:0px; ">
      <img alt="" :src="picture" width="700" height="300"/>
    </div>
    <div id="page">
      <div id="class">课程 {{ title }}</div>
      <p class="classContent">{{ classIntro }}</p>
      <div class="operate">
          <el-button type="success">{{ buttonShow }}</el-button>
      </div>
    </div>
    <div>
      <router-link to="/coursepage">
        <button>进入课程</button>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      buttonShow:"观看",
      title: '我们爱科学',
      classIntro:'科学是人类的好朋友',
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
