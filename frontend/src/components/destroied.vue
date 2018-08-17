<template>
  <div class="destroied"  style="text-align: center">
    <div id="des-outline">
      <div id="des-inner">
        <img src="../assets/images/fire.png" id="fire-img" style="width:250px">
        <div style="margin:80px auto">
          <div class="des-message">该页面已被焚毁</div>
          <br />
          <div class="des-message">下次早点来哦</div>
        </div>
        <div>
          <router-link to="/">
            <el-button id="return-index" type="text">返回首页</el-button>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {

    }
  }
}
</script>

<style scoped>
  #des-outline {
    background-color: lightgray;
    width: 500px;
    height: 700px;
    border: 1px, solid, rgb(104, 104, 104);
    border-radius: 5px;
    margin: auto;
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
  }
  #fire-image {
    position: absolute;
    margin: 50px auto;
  }
  #des-inner {
    position: absolute;
    top: 80px;
    left: 0;
    bottom: 0;
    right: 0;
  }
  .des-message {
    font-size: 28px;
    color: black;
  }
  #return-index {
    font-size:20px;
    color: #409EFF;
  }
</style>
