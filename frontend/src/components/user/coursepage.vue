<template>
  <div>
    <div class="toolbar">
      <div class="logo">
      <img src="../../assets/logo1.png" width="200%" height="100%">
      </div>
      <table align="right">
        <tr>
          <td>
            <router-link to="/personal">
              <el-button class="user_ope" type="text">个人中心</el-button>
            </router-link>
          </td>
          <td>
            <el-button class="user-ope" type="text" @click="logout">登出</el-button>
          </td>
        </tr>
      </table>
    </div>
    <el-container>
      <el-main align="center">
        <div>
          <div>
            <img :src="coursepicture1" class="coursepicture">
          </div>
          <div id="player_sharer" align="center">
            <div class="audioplayer">
              <el-row>
                <el-col :span="4">
                  <el-button
                  @click="play"
                  id="playerbutton"
                  icon="el-icon-caret-right"
                  circle></el-button>
                </el-col>
                <el-col :span="16">
                  <el-row>
                    <el-col :span="10">
                      <el-slider
                      @change="changeTime"
                      :format-tooltip="formatTime"
                      :max="music.maxTime"
                      v-model="music.currentTime"
                      ></el-slider>
                    </el-col>
                    <el-col :span="6" class="volumelabel">
                      <el-label>音量：{{ music.volume }}%</el-label>
                    </el-col>
                    <el-col :span="4">
                      <el-button
                      @click="changeVolume(-10)"
                      id="playerbutton"
                      icon="el-icon-minus"
                      circle></el-button>
                    </el-col>
                    <el-col :span="3">
                      <el-button
                      @click="changeVolume(10)"
                      id="playerbutton"
                      icon="el-icon-plus"
                      circle></el-button>
                    </el-col>
                  </el-row>
                </el-col>
                <el-col :span="4" class="audiotime">
                  {{formatTime(music.currentTime)}}/{{formatTime(music.maxTime)}}
                </el-col>
              </el-row>
              <audio ref="music" autoplay>
                <source :src="courseaudio1">
              </audio>
            </div>
            <el-button class="share" icon="el-icon-share" circle></el-button>
          </div>
          <div class="course_description">
            <h1 id="course_description" :course_description="course_description">{{ course_description }}</h1>
          </div>
          <div>
            <el-button class="leave_msg" @click="dialogVisible = true">写留言</el-button>
            <el-dialog
              title="写留言"
              :visible.sync="dialogVisible"
              width="50%"
              :before-close="handleClose"
              align="left">
              <span class="dialog_msg">在此编辑你的留言：</span>
              <el-input
                type="textarea"
                :rows="5"
                class="comment_input"
                placeholder="请输入内容"
                v-model="tempcomment">
              </el-input>
              <span slot="footer" class="dialog-footer">
                <el-button @click="dialogVisible = false">取 消</el-button>
                <el-button type="primary" @click="confirmMsg">确 定</el-button>
              </span>
            </el-dialog>
            <h2>留言区</h2>
            <div>
              <el-col class="course_msgboard" v-for="post in posts" :key="post.id">
                <div class="course_header">
                    <img :src="post.header" class="header_img">
                </div>
                <h3>{{ post.author }}</h3>
                <h4>发表于 {{ post.created_at }}</h4>
                <div class="msg_content">{{ post.content }}</div>
                <el-button id="course_dislike" icon="el-icon-arrow-down">({{ post.dislike }})</el-button>
                <el-button id="course_like" icon="el-icon-arrow-up">({{ post.like }})</el-button>
                <el-button id="course_reply_author">回复</el-button>
                <div >
                  <el-col class="course_reply" v-for="reply in post.reply" :key="reply.id">
                    <h5>{{ reply.author }}：</h5>
                    <div class="reply_content">{{ reply.content }}</div>
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
import * as utils from '../utils/utils.js'

export default {
  data() {
    return {
      coursepicture1: require('../../assets/images/course1.jpg'),
      courseaudio1: require('../../assets/audios/audio1.mp3'),
      music: {
        isPlay: false,
        currentTime: 0,
        maxTime: 0,
        volume: 100
      },
      courseid: '',
      course_description: '该课程还没有添加描述哦！',
      dialogVisible: false,
      tempcomment: '',
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
  mounted() {
    this.$nextTick(() => {
      setInterval(this.listenMusic, 1000)
    })
  },
  methods: {
    listenMusic() {
      if (!this.$refs.music) {
        return
      }
      if (this.$refs.music.readyState) {
        this.music.maxTime = this.$refs.music.duration
      }
      this.music.isPlay = !this.$refs.music.paused
      this.music.currentTime = this.$refs.music.currentTime
    },
    play() {
      if (this.$refs.music.paused) {
        this.$refs.music.play()
      } else {
        this.$refs.music.pause()
      }
      this.music.isPlay = !this.$refs.music.paused
      this.$nextTick(() => {
        document.getElementById('play').blur()
      })
    },
    changeTime(time) {
      this.$refs.music.currentTime = time
    },
    changeVolume(v) {
      this.music.volume += v
      if (this.music.volume > 100) {
        this.music.volume = 100
      }
      if (this.music.volume < 0) {
        this.music.volume = 0
      }
      this.$refs.music.volume = this.music.volume / 100
    },
    formatTime(time) {
      let it = parseInt(time)
      let m = parseInt(it / 60)
      let s = parseInt(it % 60)
      return (m < 10 ? '0' : '') + parseInt(it / 60) + ':' + (s < 10 ? '0' : '') + parseInt(it % 60)
    },
    handleClose(done) {
      this.$confirm('确认关闭？你的编辑在离开网页时将会丢失！')
        .then(_ => {
          done()
        })
        .catch(_ => {})
    }
  },
  created: function() {
    this.courseid = this.$route.params.courseid
    axios.post(utils.getURL() + 'api/coursepage/', qs.stringify({
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
  .toolbar {
    width: 100%;
    min-height: 55px;
    max-height: 70px;
    margin: 0;
    padding: 0;
    background-color:lightskyblue;
    opacity: 0.7;
  }

  .logo {
    margin-left: 50px;
    display: inline-block;
    width: 55px;
    height: 55px;
  }

  .user-ope {
    color: black;
    font-size:18px;
    margin-right: 60px;
  }
  .user_ope {
    color: black;
    font-size:18px;
    margin-right: 60px;
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

  #player_sharer {
    display: flex;
  }

  .audioplayer {
    border: 1px solid black;
    width: 36%;
    height: 50px;
    padding-top: 1%;
    border-radius: 20px;
    margin-left: 30%;
  }

  .audiotime {
    color: #909399;
    font-size: 13px;
    margin-top: 2.5%;
  }

  .volumelabel {
    font-size: 1%;
    margin-top: 3%;
    margin-left: 3%;
  }

  .share {
    height: 40px;
    margin-left: 1%;
    margin-top: 1%;
  }

  .leave_msg {
    float: right;
    margin-right: 20%;
    background-color: skyblue;
    color: blue;
  }

  .dialog_msg {
    margin-left: 10%;
  }

  .comment_input {
    width: 80%;
    margin-left: 10%;
    margin-top: 20px;
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

  @media screen and (max-width: 500px) {
    .user-ope {
      color: black;
      font-size:15px;
      margin-right: 10px;
    }
    .user_ope {
      color: black;
      font-size:15px;
      margin-right: 10px;
    }
    .toolbar {
      min-height: 42px;
    }
    .logo {
      margin-left: 30px;
      display: inline-block;
      width: 42px;
      height: 42px;
    }
  }
  </style>
