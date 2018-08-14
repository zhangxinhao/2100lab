<template>
  <div>
    <el-container>
      <el-header>
        <div class="toolbar">
          <table align="right">
            <tr>
              <td>
                <el-button class="user-ope" type="text" style="color:blue;">个人中心</el-button>
              </td>
              <td>&nbsp;&nbsp;&nbsp;&nbsp;</td>
<<<<<<< HEAD
                </tr>
                  </table>
=======
            </tr>
          </table>
>>>>>>> ad6b5d04c3d02112b1fdca5530716226efa40419
        </div>
      </el-header>
      <el-main style="text-align: center;">
        <div>
          <div>
            <img :src="coursepicture1" alt=""
            style="width: 25%; height: 25%; object-fit: contain;">
          </div>
<<<<<<< HEAD
=======
          <div>
            <audio autoplay="autoplay" controls="controls" preload="auto" :src="courseaudio1"></audio>
            <el-button><i class="el-icon-share"></i></el-button>
          </div>
>>>>>>> ad6b5d04c3d02112b1fdca5530716226efa40419
        </div>
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
<<<<<<< HEAD
    data() {
    return {
      coursepicture1: require('../assets/images/course1.jpg'),
=======
  data() {
    return {
      coursepicture1: require('../assets/images/course1.jpg'),
      courseaudio1: require('../assets/audios/audio1.mp3'),
>>>>>>> ad6b5d04c3d02112b1fdca5530716226efa40419
    }
  }
}
</script>

<style>
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
  </style>
