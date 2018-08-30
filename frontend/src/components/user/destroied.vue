<template>
  <div class="destroied">
    <div id="des-outline">
      <div id="des-inner">
        <img src="../../assets/burn1.jpg" id="fire-img">
        <div>
          <div class="des-message">该页面已被焚毁</div>
          <br />
          <div class="des-message">下次早点来哦</div>
        </div>
        <br />
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
  .destroied {
    text-align: center;
  }
  #des-outline {
    width: 500px;
    height: 700px;
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
    font-family: 'youyuan';
    font-weight: bold;
    font-size: 28px;
    color: black;
  }
  #return-index {
    font-size: 20px;
    color: #409EFF;
  }
  img {
    width: 400px;
  }
  @media screen and (max-width: 500px) {
    #des-outline {
    width: 300px;
    height: 500px;
    border-radius: 5px;
    margin: auto;
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
  }
  .des-message {
    font-family: 'youyuan';
    font-size: 18px;
    color: black;
    margin: 0px;
  }
  #return-index {
    font-size: 15px;
    color: #409EFF;
  }
  img {
    width: 200px;
  }
  .element-style {
    margin: 10px !important;
  }
}
</style>
