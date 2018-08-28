<template>
  <div class="course-page">
    <div class="tool-bar">
      <router-link to="/">
        <div class="logo">
          <img src="../../assets/logo3.png" width="200%" height="80%">
        </div>
      </router-link>
      <table align="right">
        <tr>
          <td>
            <router-link to="/personal">
              <el-button
                class="user-ope"
                type="text"
                v-if="login">
                个人中心
              </el-button>
            </router-link>
          </td>
          <td>
            <el-button class="user-ope"
              type="text"
              v-if="!login"
              @click="loginFormVisible = true">登录<br><br>
            </el-button>
          </td>
          <td>
            <el-button
              class="user-ope"
              type="text"
              v-if="login"
              @click="logout">
              登出
            </el-button>
          </td>
        </tr>
      </table>
    </div>

    <div class="login-dialog">
      <el-dialog
        title="登录"
        :visible.sync="loginFormVisible"
        class="lodialog"
        width="330px"
        height="500px">
        <el-form :model="loForm" :rules="rules">
          <el-form-item
            label="手机号"
            :label-width="loginLabelWidth"
            prop="loPhone">
            <el-col :span="18">
              <el-input
                v-model="loForm.phoneNumber"
                auto-complete="true"
                clearable
                required="required"
                pattern="/^1[3|4|5|7|8][0-9]\d{8}$/"
                oninvalid="this.setCustomValidity('warning')">
              </el-input>
            </el-col>
          </el-form-item>
          <el-form-item
            label="验证码"
            :label-width="loginLabelWidth">
            <el-col :span="18">
              <el-input
                v-model="loForm.usercode"
                auto-complete="off"
                clearable>
              </el-input>
            </el-col>
          </el-form-item>
        </el-form>
        <div slot="footer" class="login-footer">
          <el-button type="primary">获取验证码</el-button>
          <el-button @click="loginFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="loginFormVisible = false">
            确 定
          </el-button>
        </div>
      </el-dialog>
    </div>

    <div class="main-container">

      <div v-for="pic in coursePic" :key="pic.id">
        <link rel="preload" :href="pic.position" as="image">
      </div>

      <div>
        <link rel="preload" :href="courseAudio" as="audio">
      </div>

      <div class="img-container">
        <img :src="nowPic.position" class="course-pic">
      </div>

      <div class="audio-container">
        <el-row class="hidden-md-and-down">
          <el-col :span="2">
            <el-button id="play-btn" type="primary" circle @click="play">
              <i class="iconfont icon-bofang" v-if="!music.isPlay"></i>
              <i class="iconfont icon-zanting" v-else></i>
            </el-button>
          </el-col>
          <el-col :span="12">
            <el-slider
              v-model="music.currentTime"
              :max="music.maxTime"
              :format-tooltip="formatTime"
              @change="changeTime">
            </el-slider>
          </el-col>
          <el-col :span="4">
            <div class="word-in">
              {{formatTime(music.currentTime)}}/{{formatTime(music.maxTime)}}
            </div>
          </el-col>
          <el-col :span="2">
            <div class="word-in">
              <span id="voice">音量：</span>
            </div>
          </el-col>
          <el-col :span="4">
            <el-slider
              v-model="music.volume"
              :format-tooltip="formatVoice"
              @change="changeVoice">
            </el-slider>
          </el-col>
        </el-row>

        <el-row class="hidden-lg-and-up">
          <el-col :span="2">
            <el-button id="play-btn" type="primary" circle @click="play">
              <i class="iconfont icon-bofang" v-if="!music.isPlay"></i>
              <i class="iconfont icon-zanting" v-else></i>
            </el-button>
          </el-col>
          <el-col :span="22">
            <el-slider
              v-model="music.currentTime"
              :max="music.maxTime"
              :format-tooltip="formatTime"
              @change="changeTime">
            </el-slider>
          </el-col>
        </el-row>

        <audio ref="music" autoplay>
          <source :src="courseAudio">
        </audio>
      </div>

      <div class="artical-container">
        {{ courseArtical }}
      </div>

      <div class="share-container">
        <i class="el-icon-share"></i><span>分享到</span>
        <share :config="config" class="share"></share>
      </div>
    </div>

    <div class="discuss-container">
      <div class="discuss-header">
        <h1 class="hidden-md-and-down">评论区</h1>
        <h3 class="hidden-lg-and-up">评论区</h3>
      </div>
      <div class="write-discuss">
        <el-input
          type="textarea"
          :rows="4"
          placeholder="请输入内容"
          v-model="discussWord">
        </el-input>
      </div>

      <div class="discuss-btn">
        <el-button type="primary" icon="el-icon-edit" @click="leaveDiscussion">
          发表
        </el-button>
        <el-button
          icon="el-icon-delete"
          @click="discussWord = ''">
          清空
        </el-button>
      </div>

      <div class="discuss-area">
        <div v-for="item in onePageDiscussion" :key="item.id">
          <el-container>
            <el-aside class="userImg-container">
              <el-row>
                <img :src="item.userImg" class="userImg">
              </el-row>
              <el-row class="reply-user">
                <div>
                  {{ item.userName }}
                  <i v-if="item.userType" class="iconfont icon-myvip"></i>
                </div>
              </el-row>
            </el-aside>
            <el-container>
              <el-header class="discussion">
                <el-row class="disMes">
                  <el-col :span=24>
                    {{ item.discussMessage }}
                  </el-col>
                </el-row>
                <el-row>
                  <el-col :span="9" :xs="12" :sm="12" :md="12" :lg="9" :xl="9">
                    <el-button
                      icon="el-icon-time"
                      type="text"
                      color="black">
                      {{ item.discussTime }}
                    </el-button>
                  </el-col>
                  <el-col :span="3" :xs="4" :sm="4" :md="4" :lg="3" :xl="3">
                    <el-button
                      icon="el-icon-caret-top"
                      type="text"
                      @click="leaveAttitude(item, 'like')">
                      赞
                    </el-button>
                    <span class="hidden-md-and-down">
                      : {{ item.likeNum }}
                    </span>
                  </el-col>
                  <el-col :span="3" :xs="4" :sm="4" :md="4" :lg="3" :xl="3">
                    <el-button
                      icon="el-icon-caret-bottom"
                      type="text"
                      @click="leaveAttitude(item, 'dislike')">
                      踩
                    </el-button>
                    <span class="hidden-md-and-down">
                      : {{ item.dislikeNum }}
                    </span>
                  </el-col>
                  <el-col :span="3">
                    <el-button
                      icon="el-icon-plus"
                      type="text"
                      @click="item.addReply=!item.addReply">
                      回复
                    </el-button>
                  </el-col>
                </el-row>
              </el-header>
              <el-main class="indis-container">
                <el-row v-for="initem in item.indiscussion" :key="initem.id">
                  <el-col :span="8">
                    {{ initem.userName }}
                    <div
                      class="re-reply-type"
                      v-if="initem.userType">
                      <i class="iconfont icon-myvip"></i>
                    </div>
                  </el-col>
                  <el-col>
                    <div>:{{ initem.indisMessage }}</div>
                  </el-col>
                  <el-col>
                    <br />
                  </el-col>
                </el-row>
                <el-row v-if="item.addReply">
                  <div class="write-reply">
                    <el-input
                      type="textarea"
                      :rows="4"
                      placeholder="请输入内容"
                      v-model="item.replyMsg">
                    </el-input>
                  </div>
                  <div class="reply-btn">
                    <el-button
                      type="primary"
                      icon="el-icon-edit"
                      @click="leaveComment(item)">
                      发表
                    </el-button>
                    <el-button
                      icon="el-icon-delete"
                      @click="item.replyMsg=''">
                      清空
                    </el-button>
                  </div>
                </el-row>
              </el-main>
            </el-container>
          </el-container>
          <hr />
        </div>
      </div>

      <div class="pager-container">
        <el-pagination
          background
          small
          layout="prev, pager, next"
          :page-size="pageSize"
          :total="totalNumber"
          :current-page.sync="pageNo"
          :pager-count="7"
          @current-change="flipeOver">
        </el-pagination>
      </div>
    </div>
    <div class="hidden-md-and-down" id="footer">
      <img src="../../assets/footer1.png" width=100%>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import qs from 'qs'
import * as utils from '../utils/utils.js'

export default {
  data: function() {
    let phoneReg = /^1[3|4|5|7|8][0-9]\d{8}$/
    let validateloPhone = (rule, value, callback) => {
      if (!this.loForm.phoneNumber) {
        return callback(new Error('号码不能为空'))
      }
      setTimeout(() => {
        if (!phoneReg.test(this.loForm.phoneNumber)) {
          callback(new Error('格式有误'))
        } else {
          callback()
        }
      }, 100)
    }
    return {
      user: '999',
      sharePerson: '',
      burntTime: 999999999999,
      login: true,
      loginFormVisible: false,
      loginLabelWidth: '100px',
      loForm: {
        phoneNumber: '',
        password: '',
        delivery: false,
        usercode: ''
      },
      rules: {
        loPhone: [
          {
            required: true,
            validator: validateloPhone,
            trigger: 'blur'
          }
        ]
      },
      tempCourse: [],
      tempPictures: [],
      coursePic: [
        {
          position: require('../../assets/images/1-1.001.png'),
          start: 0
        },
        {
          position: require('../../assets/images/1-1.002.png'),
          start: 8
        },
        {
          position: require('../../assets/images/1-1.003.png'),
          start: 38
        },
        {
          position: require('../../assets/images/1-1.004.png'),
          start: 72
        },
        {
          position: require('../../assets/images/1-1.005.png'),
          start: 100
        },
        {
          position: require('../../assets/images/1-1.006.png'),
          start: 114
        }
      ],
      nowPic: {},
      courseAudio: require('../../assets/audios/1.mp3'),
      music: {
        isPlay: false,
        currentTime: 0,
        maxTime: 0,
        volume: 100
      },
      courseId: '',
      courseArtical: '你好啊',
      config: {
        url: '', // 网址，默认使用 window.location.href
        sites: ['qzone', 'qq', 'weibo', 'wechat'] // 启用的站点
      },
      discussWord: '',
      discussionList: [],
      onePageDiscussion: [
        {
          userName: 'gyy',
          userImg: require('../../assets/images/userImg.jpg'),
          userType: false,
          discussTime: '2018.8.22 19:00',
          discussMessage: '啦啦啦啦啦啦啦啦啦啦',
          likeNum: 0,
          dislikeNum: 0,
          addReply: false,
          replyMsg: '',
          indiscussion: [
            {
              userName: 'zyfcka',
              userType: true,
              indisMessage: 'mdzz'
            },
            {
              userName: 'dyf',
              userType: true,
              indisMessage: 'mdzz'
            }
          ]
        },
        {
          userName: 'lyx',
          userImg: require('../../assets/images/userImg2.jpg'),
          userType: true,
          discussTime: '2018.8.22 20:00',
          discussMessage: '我超聪明你超笨',
          likeNum: 0,
          dislikeNum: 0,
          addReply: false,
          replyMsg: '',
          indiscussion: [
            {
              userName: 'hyl',
              userType: false,
              indisMessage: '我超聪明你超笨'
            }
          ]
        }
      ],
      pageSize: 12,
      totalNumber: 100,
      pageNo: 1,
      interValId: 0
    }
  },
  mounted: function() {
    this.$nextTick(() => {
      this.interValId = setInterval(this.imgplay, 500)
    })
  },
  beforeDestroy: function() {
    clearInterval(this.interValId)
    axios.post(utils.getURL() + 'api/feedbackrecord/', qs.stringify({
      courseId: this.courseId,
      last_time: this.music.currentTime
    })).then(response => {})
  },
  methods: {
    imgplay: function() {
      let time = new Date().getTime()
      if (this.burntTime < time / 1000) {
        this.$router.push({path: '/intro/' +
          this.courseId + '/' + this.user})
      }
      let i = 0
      for (i = 0; i < this.coursePic.length; i++) {
        if (this.coursePic[i].start > parseInt(this.$refs.music.currentTime)) {
          break
        }
      }
      this.nowPic = this.coursePic[i - 1]
      this.listenMusic()
    },
    listenMusic: function() {
      if (!this.$refs.music) {
        return
      }
      if (this.$refs.music.readyState) {
        this.music.maxTime = this.$refs.music.duration
      }
      this.music.isPlay = !this.$refs.music.paused
      this.music.currentTime = this.$refs.music.currentTime
    },
    play: function() {
      if (this.$refs.music.paused) {
        this.$refs.music.play()
      } else {
        this.$refs.music.pause()
      }
      this.music.isPlay = !this.$refs.music.paused
    },
    changeTime: function(time) {
      this.$refs.music.currentTime = time
    },
    formatTime: function(time) {
      let it = parseInt(time)
      let m = parseInt(it / 60)
      let s = parseInt(it % 60)
      return (m < 10 ? '0' : '') + parseInt(it / 60) +
        ':' + (s < 10 ? '0' : '') + parseInt(it % 60)
    },
    logout: function() {
      this.login = false
    },
    formatVoice: function(val) {
      return this.music.volume
    },
    changeVoice: function(val) {
      this.music.volume = val
      this.$refs.music.volume = this.music.volume / 100
    },
    leaveDiscussion: function() {
      let msgReg = /^[\s\t\n]*$/
      if (msgReg.test(this.discussWord)) {
        this.$message({
          message: '发表内容不能为空！',
          type: 'warning'
        })
        this.discussWord = ''
      } else {
        axios.post(utils.getURL() + 'api/leaveMessage/', qs.stringify({
          course_id: this.$route.params.courseid,
          content: this.discussWord
        })).then(response => {
          if (response.data.status === 1) {
            this.$message.error('无法发表评论！您已被系统禁言！')
            return
          }
          this.discussionList = []
          let tempmessage = response.data.message
          this.refresh(tempmessage)
        })
      }
    },
    leaveComment: function(msg) {
      let msgReg = /^[\s\t\n]*$/
      if (msgReg.test(msg.replyMsg)) {
        this.$message({
          message: '回复内容不能为空！',
          type: 'warning'
        })
        msg.replyMsg = ''
      } else {
        axios.post(utils.getURL() + 'api/comment/', qs.stringify({
          course_id: this.$route.params.courseid,
          message_id: msg.messageId,
          content: msg.replyMsg
        })).then(response => {
          if (response.data.status === 1) {
            this.$message.error('无法发表回复！您已被系统禁言！')
            return
          }
          this.discussionList = []
          let tempmessage = response.data.message
          this.refresh(tempmessage)
        })
      }
    },
    leaveAttitude: function(msg, attitude) {
      axios.post(utils.getURL() + 'api/attitude/', qs.stringify({
        course_id: this.$route.params.courseid,
        message_id: msg.messageId,
        attitude: attitude
      })).then(response => {
        this.discussionList = []
        let tempmessage = response.data.message
        this.refresh(tempmessage)
      })
    },
    flipeOver: function (page) {
      let _end = this.pageSize * page
      let end = this.totalNumber < (_end) ? this.totalNumber : _end
      this.freeList = []
      let start = this.pageSize * (page - 1)
      for (let i = start; i < end; i++) {
        this.freeList.push(this.courses[i])
      }
    },
    initialize(course, pictures, message) {
      let length = pictures.length
      let tempPicture = {
        position: '',
        start: ''
      }
      this.coursePic = []
      for (let i = 0; i < length; i++) {
        tempPicture.position = utils.getURL() + 'media/' +
          pictures[i].fields.postion
        tempPicture.start = pictures[i].fields.start
        this.coursePic.push(tempPicture)
      }
      this.courseAudio = utils.getURL() + 'media/' +
        course.audio_url
      this.courseArtical = course.content
      this.refresh(message)
    },
    refresh(message) {
      for (let i = 0; i < message.length; i++) {
        this.discussionList.push({
          'userImg': utils.getURL() + 'media/' +
            message[i].icon,
          'discussTime': message[i].time,
          'userName': message[i].author,
          'discussMessage': message[i].content,
          'indiscussion': message[i].reply,
          'likeNum': message[i].likes,
          'dislikeNum': message[i].dislikes,
          'userType': message[i].usertype,
          'messageId': message[i].message_id
        })
      }
      this.totalNumber = this.discussionList.length
      let totalNumber = this.totalNumber
      this.onePageDiscussion = []
      let size = this.pageSize
      if (totalNumber < size) {
        this.onePageDiscussion = this.discussionList
      } else {
        for (let i = 0; i < size; i++) {
          this.onePageDiscussion.push(this.discussionList[i])
        }
      }
    }
  },
  created: function() {
    this.courseId = this.$route.params.courseid
    this.sharePerson = this.$route.params.user
    this.user = this.$store.state.userId
    this.config.url = utils.getURL() + '#/intro/' +
      this.courseId + '/' + this.user
    this.nowPic = this.coursePic[0]
    axios.post(utils.getURL() + 'api/coursepage/', qs.stringify({
      course_id: this.$route.params.courseid
    })).then(response => {
      this.discussionList = []
      this.onePageDiscussion = []
      this.coursePic = []
      this.tempCourse = response.data.course[0].fields
      this.tempPictures = response.data.pictures
      let tempMessage = response.data.message
      this.initialize(this.tempCourse, this.tempPictures, tempMessage)
    })
    axios.post(utils.getURL() + 'api/checkrecord/', qs.stringify({
      courseId: this.$route.params.courseid
    })).then(response => {
      this.$refs.music.currentTime = response.data.lastTime
      this.burntTime = response.data.dealVisitTime
    })
  }
}
</script>

<style scoped>
  .course-page {
    background-color: rgb(240, 240, 240);
  }
  .tool-bar {
    width: 100%;
    min-height: 45px;
    max-height: 70px;
    padding: 0;
    background-color:#409EFF;
  }

  .logo {
    margin-left: 50px;
    display: inline-block;
    width: 55px;
    height: 55px;
  }
  #footer {
    color: #333;
    text-align: center;
    line-height: 55px;
  }
  .user-ope {
    color: white;
    font-size:18px;
    margin-right: 60px;
  }
  .el-main {
    padding-bottom: 0 !important;
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
  hr {
    height: 2px;
    border: none;
    background: rgb(233, 233, 233);
  }
  .main-container {
    max-width: 1200px;
    margin: 20px auto;
  }
  .img-container {
    width: 700px;
    height: 500px;
    margin: 20px auto 0 auto;
    text-align:center;
    vertical-align: middle;
  }
  .course-pic {
    width: 90%;
    height: 90%;
    object-fit: contain;
    position: relative;
    top: 50%;
    transform: translate(0,-50%);
  }
  .audio-container {
    width: 900px;
    height: 60px;
    margin: 50px auto 50px auto;
    text-align: center;
    vertical-align: middle;
  }
  .icon-bofang:before {
    font-size: 25px;
  }
  .icon-zanting:before {
    font-size: 25px;
  }
  .icon-myvip:before {
    font-size: 20px;
    color: #409EFF;
  }
  .word-in {
    margin-top: 16px;
  }
  .el-slider {
    display: inline-block;
    width: 90%;
    margin: 7px auto;
  }
  #voice {
    margin: 20px auto auto auto;
  }
  .artical-container {
    width: 630px;
    margin: 20px auto 0 auto;
    font-size: 20px;
    line-height: 40px;
    text-indent:2em;
  }
  .share-container {
    width: 900px;
    margin: 80px auto 150px auto;
    text-align: right;
  }
  .discuss-container {
    width: 1200px;
    min-height: 1000px;
    margin: 20px auto;
  }
  .discuss-header {
    width: 900px;
    height: 100px;
    margin: 0 auto 5px auto;
    text-align: left;
  }
  .write-discuss {
    width: 700px;
    margin: 0 auto;
  }
  .discuss-btn {
    width: 900px;
    text-align: right;
    margin: 30px auto;
  }
  .discuss-area {
    width: 900px;
    margin: 30px auto;
  }
  .userImg-container {
    width: 100px !important;
  }
  .userImg {
    width: 100%;
  }
  .discussion {
    min-height: 100px;
  }
  .disMes {
    min-height: 65px;
    margin: 5px auto 5px auto;
  }
  .indis-container {
    margin-top: 20px;
  }
  .pager-container {
    text-align: right;
  }
  .write-reply {
    width: 500px;
    margin: 30px auto;
  }
  .reply-btn {
    width: 700px;
    text-align: right;
    margin: 10px auto;
  }
  .share {
    display: inline;
  }
  .reply-user {
    text-align: center;
  }
  .re-reply-type {
    display: inline;
  }

  @media screen and (max-width: 500px) {
    .icon-bofang:before {
      font-size: 16px;
    }
    .icon-zanting:before {
      font-size: 16px;
    }
    .user-ope {
      color: white;
      font-size:15px;
      margin-right: 10px;
    }
    .tool-bar {
      min-height: 42px;
    }
    .logo {
      margin-left: 30px;
      display: inline-block;
      width: 42px;
      height: 42px;
    }
    hr {
      height: 1px;
      border: none;
      background: rgb(233, 233, 233);
    }
    .img-container {
      width: 300px;
      height: 215px;
      margin: 20px auto 0 auto;
      text-align: center;
      vertical-align: middle;
    }
    .audio-container {
      width: 350px;
      height: 50px;
      margin: auto auto 10px auto;
      text-align: center;
      vertical-align: middle;
    }
    .artical-container {
      width: 300px;
      margin: 20px auto 0 auto;
      font-size: 18px;
    }
    .share-container {
      width: 350px;
      margin: 50px auto 80px auto;
      text-align: right;
    }
    .discuss-container {
      max-width: 350px;
      max-height: 600px;
      margin: 20px auto;
    }
    .discuss-header {
      max-width: 350px;
      height: 50px;
      margin: 0 auto 5px auto;
      text-align: left;
    }
    .write-discuss {
      max-width: 300px;
      margin: 0 auto;
    }
    .discuss-btn {
      max-width: 350px;
      text-align: right;
      margin: 30px auto;
    }
    .discuss-area {
      max-width: 350px;
      margin: 30px auto;
    }
    .userImg-container {
      max-width: 50px !important;
    }
    .discussion {
      min-height: 50px;
    }
    .disMes {
      min-height: 40px;
      margin: 5px auto 5px auto;
    }
    .indis-container {
      margin-top: 20px;
    }
    .pager-container {
      text-align: right;
    }
    .write-reply {
      width: 250px;
      margin: 10px auto;
    }
    .reply-btn {
      width: 280px;
      text-align: right;
      margin: 10px auto;
    }
  }

  @media screen and (min-width: 500px) and (max-width: 1100px) {
    .user-ope {
      color: white;
      font-size:15px;
      margin-right: 10px;
    }
    .tool-bar {
      min-height: 42px;
    }
    .logo {
      margin-left: 30px;
      display: inline-block;
      width: 42px;
      height: 42px;
    }
    hr {
      height: 1px;
      border: none;
      background: rgb(233, 233, 233);
    }
    .img-container {
      width: 500px;
      height: 350px;
      margin: 20px auto 0 auto;
      text-align: center;
      vertical-align: middle;
    }
    .audio-container {
      width: 600px;
      height: 50px;
      margin: auto auto 10px auto;
      text-align: center;
      vertical-align: middle;
    }
    .artical-container {
      width: 500px;
      margin: 20px auto 0 auto;
      font-size: 18px;
    }
    .share-container {
      width: 600px;
      margin: 50px auto 80px auto;
      text-align: right;
    }
    .discuss-container {
      max-width: 600px;
      max-height: 2000px;
      margin: 20px auto;
    }
    .discuss-header {
      max-width: 600px;
      height: 50px;
      margin: 0 auto 5px auto;
      text-align: left;
    }
    .write-discuss {
      max-width: 500px;
      margin: 0 auto;
    }
    .discuss-btn {
      max-width: 600px;
      text-align: right;
      margin: 30px auto;
    }
    .discuss-area {
      max-width: 500px;
      margin: 30px auto;
    }
    .userImg-container {
      max-width: 50px !important;
    }
    .discussion {
      min-height: 50px;
    }
    .disMes {
      min-height: 40px;
      margin: 5px auto 5px auto;
    }
    .indis-container {
      margin-top: 20px;
    }
    .pager-container {
      text-align: right;
    }
    .write-reply {
      width: 400px;
      margin: 10px auto;
    }
    .reply-btn {
      width: 450px;
      text-align: right;
      margin: 10px auto;
    }
  }
  </style>
