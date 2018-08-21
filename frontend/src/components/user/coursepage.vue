<template>
  <div>
    <el-container>
      <el-header>
        <div class="course_toolbar">
          <table align="right">
            <tr>
              <td>
                <router-link to="/personal">
                  <el-button class="user_ope" type="text">个人中心</el-button>
                </router-link>
              </td>
              <td>&nbsp;&nbsp;&nbsp;&nbsp;</td>
            </tr>
          </table>
        </div>
      </el-header>
      <el-main align="center">
        <div>
          <div>
            <img :src="coursepicture1" class="coursepicture">
          </div>
          <div>
            <audio autoplay="autoplay" controls="controls" preload="auto" :src="courseaudio1"></audio>
            <el-button class="share_button" icon="el-icon-share"></el-button>
          </div>
          <div class="course_description">
            <h1 id="course_description" :course_description="course_description">{{ course_description }}</h1>
          </div>
          <div>
            <el-button class="leave_msg">写留言</el-button>
            <h2>留言区</h2>
            <div>
              <el-col class="course_msgboard" v-for="post in posts" :key="post.id">
                <div class="course_header">
                    <img :src="post.header" class="header_img">
                </div>
                <h3>{{ post.author }}</h3>
                <h4>发表于 {{ post.created_at }}</h4>
                <div class="msg_content">{{ post.content }} </div>
                <el-button id="course_dislike" icon="el-icon-arrow-down">({{ post.dislike }})</el-button>
                <el-button id="course_like" icon="el-icon-arrow-up">({{ post.like }})</el-button>
                <el-button id="course_reply_author">回复</el-button>
                <div >
                  <el-col class="course_reply" v-for="reply in post.reply" :key="reply.id">
                    <h5>{{ reply.author }}：</h5>
                    <div class="reply_content">{{ reply.content }} </div>
                  </el-col>
                </div>
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
import axios from 'axios'
import qs from 'qs'

export default {
  data() {
    return {
      coursepicture1: require('../../assets/images/course1.jpg'),
      courseaudio1: require('../../assets/audios/audio1.mp3'),
      courseid: '',
      course_description: '该课程还没有添加描述哦！',
      tempcourse: [],
      posts: [
        {header: require('../../assets/images/header2.jpg'),
          created_at: '2018-8-14',
          author: 'UJoe',
          content: 'just a test.just a test.just a test.just a test.just a test.just a test.just a test.just a test.just a test.just a test.just a test.just a test.just a test.just a test.just a test.just a test.just a test.just a test.just a test.just a test.just a test.just a test.just a test.just a test.just a test.just a test.just a test.just a test.just a test.',
          reply: [
            {author: 'Leeroy', content: 'Long time no see'},
            {author: 'Zombi', content: 'Long ...brain'}
          ],
          like: '5',
          dislike: '0'},
        {header: require('../../assets/images/header1.jpg'),
          created_at: '2018-8-15',
          author: 'Zombi',
          content: 'I just want your brain.',
          like: '1',
          dislike: '4'},
        {header: require('../../assets/images/header3.jpg'),
          created_at: '2018-8-15',
          author: 'Leeroy',
          content: 'I like this audio~',
          like: '12',
          dislike: '0'}
      ]
    }
  },
  methods: {
  },
  created: function() {
    this.courseid = this.$route.params.courseid
    axios.post('http://192.168.55.33:8000/api/coursepage/', qs.stringify({
      course_id: this.$route.params.courseid
    })).then(response => {
      this.posts = []
      this.tempcourse = response.data.course
      this.coursepicture1 = this.tempcourse.pictures
      this.courseaudio1 = this.tempcourse.audio
      this.course_description = this.tempcourse.course_description
      for (let i = 0; i < this.tempcourse.lenth; i++) {
        this.posts.push({
          'header': this.tempcourse.message.icon,
          'create_at': this.tempcourse.message.time,
          'author': this.tempcourse.message.author,
          'content': this.tempcourse.message.content,
          'reply': this.tempcourse.message.reply,
          'like': this.tempcourse.message.likes,
          'dislike': this.tempcourse.message.dislikes
        })
      }
    })
  }
}
</script>

<style scoped>
  .course_toolbar {
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

  .user_ope {
    color: blue;
  }

  .coursepicture {
    width: 25%;
    height: 25%;
    object-fit: contain;
  }

  .course_description {
    width:40%;
    height: 40%;
    position: relative; left: 30%;
    overflow: hidden;
    word-break: break-all; word-wrap: break-word;
    border: 3px solid blue;
    border-radius: 4px;
    margin-top: 20px;
    color: skyblue;
  }

  .share_button {
    width: 50px;
    height: 40px;
    vertical-align: 100%;
  }

  .leave_msg {
    float: right;
    margin-right: 20%;
    background-color: skyblue;
    color: blue;
  }

  .course_msgboard {
    text-align: left;
    margin-left: 20%;
    width: 60%;
    border: 1px solid black;
    margin-bottom: 3%;
    border-radius: 4px;
    padding-bottom: 2%;
  }

  .course_reply {
    text-align: left;
    margin-left: 5%;
    width: 90%;
    border: 1px solid moccasin;
    border-radius: 4px;
    margin-top: 3%;
  }

  .course_header {
    width: 50px;
    height: 50px;
    border-radius: 300px;
    overflow: hidden;
    float: left;
    border: 3px solid skyblue;
  }

  .header_img {
    width: 100%;
    height: 100%;
    object-fit: fill;
  }

  .msg_content {
    margin-left: 40px;
  }

  .reply_content {
    margin-left: 40px;
    margin-bottom: 3%;
  }

  #course_reply_author {
    width: 10%;
    height: 7%;
    font-size: 5%;
    float: right;
    margin-right: 1%;
  }

  #course_like {
    width: 10%;
    height: 7%;
    font-size: 5%;
    float: right;
    margin-right: 2%;
  }

  #course_dislike {
    width: 10%;
    height: 7%;
    font-size: 5%;
    float: right;
    margin-right: 2%;
  }

  h2 {
    color: blue;
    margin-left: 25%;
  }

  h3 {
    margin-left: 8%;
  }
  </style>
