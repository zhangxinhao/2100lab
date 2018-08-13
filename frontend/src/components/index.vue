<!-- Add "scoped" attribute to limit CSS to this component only -->
<template>

  <div class="index">
    <div class="toolbar">
      <table align="right">
        <tr>
          <td>
            <el-button class="user-ope" type="text" v-if="login" @click="loginFormVisible = true" style="color:#085078;font-size:18px">登录&nbsp;&nbsp;&nbsp;</el-button>
          </td>
          <td>
            <el-button class="user-ope" type="text" v-if="login" @click="registerFormVisible = true" style="color:#085078;font-size:18px">注册</el-button>
          </td>
          <td>
            <el-button class="user-ope" type="text" v-if="not_login" @click="logout" style="color:white">登出</el-button>
          </td>
          <td>&nbsp;&nbsp;&nbsp;&nbsp;</td>
        </tr>
      </table>
    </div>

    <div class="carousel">
      <el-carousel :interval="4000" type="card" height="500px">
        <el-carousel-item v-for="item in imgList" :key="item.id">
          <el-row>
            <el-col :span="24"><img ref="500px" :src="item.idView" class="banner_img"/></el-col>
          </el-row>
        </el-carousel-item>
      </el-carousel>
    </div>

  </div>
</template>

<script>
export default {
  data() {
    return {
      imgList: [
        {id: 0, idView: require('../assets/images/banner1.jpg')},
        {id: 1, idView: require('../assets/images/banner1.jpg')},
        {id: 2, idView: require('../assets/images/banner1.jpg')}
      ],
      login: true,
      not_login: false
    }
  },
  methods: {

  }
}
</script>

<style>
  body {
    margin: 0;
  }

  #app {
    margin: 0;
    padding: 0;
  }

  #user-ope {
    margin-right: 100px;
   }

  .index {
    margin: 0;
    padding: 0;
  }

  .toolbar {
    width: 100%;
    height: 55px;
    margin: 0;
    padding: 0;
    text-align: right;
    background-color:lightskyblue;
    background: linear-gradient(lightskyblue, white);
    opacity: 0.7;
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
  }

  .carousel {
    width: 1500px;
    text-align: center;
    margin: 20px auto;
  }
  .banner_img {
    height: 100%;
  }

</style>
