<!-- Add "scoped" attribute to limit CSS to this component only -->
<template>

  <div class="index">
    <div class="toolbar">
      <table align="right">
        <tr>
          <td>
          </td>
          <td>

          </td>
          <td>

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
      ]
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
