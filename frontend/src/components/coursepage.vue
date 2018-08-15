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
            </tr>
          </table>
        </div>
      </el-header>
      <el-main style="text-align: center;">
        <div>
          <div>
            <img :src="coursepicture1" alt=""
            style="width: 25%; height: 25%; object-fit: contain;">
          </div>
          <div>
            <audio autoplay="autoplay" controls="controls" preload="auto" :src="courseaudio1"></audio>
            <el-button style="width: 50px; height: 40px;"><i class="el-icon-share" style="vertical-align:100%;"></i></el-button>
          </div>
          <div class="description">
            <h1 id="course_description" :course_description="course_description"
            style="color: skyblue;">{{ course_description }}</h1>
          </div>
          <div>
            <h2 style="color: blue;">留言区</h2>
            <div>
              <el-col class="msgboard" v-for="post in posts" :key="post.id">
                <div class="header">
                    <img :src="post.header" style="width: 100%; height: 100%;object-fit: fill;">
                </div>
                <h3 style="margin-left:8%;">{{ post.author }}</h3>
                <h4>发表于 {{ post.created_at }}</h4>
                <hr>
              </el-col>
            </div>
          </div>
        </div>
      </el-main>
      <el-footer height="50px">2100实验室 联系电话：010-86398756 关注我们：微信服务号：科学队长</el-footer>
    </el-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      coursepicture1: require('../assets/images/course1.jpg'),
      courseaudio1: require('../assets/audios/audio1.mp3'),
      course_description: '该课程还没有添加描述哦！',
      posts: [
        {header: require('../assets/images/header2.jpg'), created_at: '2018-8-15 11:00', author: 'UJoe'},
      ],
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

  .el-footer {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 55px;
    background-color:lightskyblue;
    background: linear-gradient(white, lightskyblue);
    opacity: 0.7;
  }

  .description {
    width:40%; 
    height: 40%;
    position: relative; left: 30%;
    overflow: hidden;
    word-break: break-all; word-wrap: break-word;
    border: 3px solid blue;
    border-radius: 4px;
    margin-top: 20px;
  }

  .msgboard {
    text-align: left;
    margin-left: 20%;
    width: 60%;
  }

  .header {
    width: 50px;
    height: 50px;
    border-radius: 300px;
    overflow: hidden; 
    float: left;
    border: 3px solid skyblue;
  }
  </style>
