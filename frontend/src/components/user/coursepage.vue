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
              <el-button class="user-ope" type="text" v-if="login">个人中心</el-button>
            </router-link>
          </td>
          <td>
            <el-button class="user-ope" type="text" v-if="!login" @click="loginFormVisible = true">登录/注册&nbsp;&nbsp;</el-button>
          </td>
          <td>
            <el-button class="user-ope" type="text" v-if="login" @click="logout">登出</el-button>
          </td>
        </tr>
      </table>
    </div>

    <div class="logindialog">
      <el-dialog title="登录" :visible.sync="loginFormVisible" class="lodialog" width="330px" height="500px">
        <el-form :model="loform" :rules="rules">
          <el-form-item label="手机号" :label-width="loginLabelWidth" prop="lophone">
            <el-col :span="18">
              <el-input v-model="loform.phonenumber" auto-complete="true" clearable required="required" pattern="/^1[3|4|5|7|8][0-9]\d{8}$/" oninvalid="this.setCustomValidity('warning')"></el-input>
            </el-col>
          </el-form-item>
          <el-form-item label="验证码" :label-width="loginLabelWidth">
            <el-col :span="18">
              <el-input v-model="loform.usercode" auto-complete="off" clearable></el-input>
            </el-col>
          </el-form-item>
        </el-form>
        <div slot="footer" class="login-footer">
          <el-button type="primary">获取验证码</el-button>
          <el-button @click="loginFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="loginFormVisible = false">确 定</el-button>
        </div>
      </el-dialog>
    </div>

    <div class="main-container">

      <div class="img-container">
        <img :src="coursePic" class="coursePic">
      </div>

      <div class="audio-container">
        <el-row class="hidden-md-and-down">
          <el-col :span="2">
            <el-button id="play-btn" type="primary" circle>
              <i class="el-icon-caret-right" width="30px" height="30px"></i>
            </el-button>
          </el-col>
          <el-col :span="16">
            <el-slider v-model="playTime" :format-tooltip="formatTime"></el-slider>
          </el-col>
          <el-col :span="2">
            <span id="voice">音量：</span>
          </el-col>
          <el-col :span="4">
            <el-slider v-model="music.volume" :format-tooltip="formatVoice"></el-slider>
          </el-col>
        </el-row>

        <el-row class="hidden-lg-and-up">
          <el-col>
            <el-slider v-model="playTime" :format-tooltip="formatTime"></el-slider>
          </el-col>
        </el-row>
      </div>

      <div class="artical-container">
        {{ course_artical }}
      </div>

      <div class="share-container">
        <i class="el-icon-share"></i><span>分享到</span>
        <share :config="config" style="display:inline"></share>
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
        <el-button type="primary" icon="el-icon-edit">发表</el-button>
        <el-button icon="el-icon-delete">清空</el-button>
      </div>

      <div class="discuss-area">
        <div v-for="item in discussionList" :key="item.id">
          <el-container>
            <el-aside class="userImg-container">
              <el-row>
                <img :src="item.userImg" class="userImg">
              </el-row>
              <el-row style="text-align:center">
                <div>{{ item.userName }}</div>
                <div v-if="item.userType">V</div>
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
                    <el-button icon="el-icon-time" type="text" style="color: black">{{ item.discussTime }}</el-button>
                  </el-col>
                  <el-col :span="3" :xs="4" :sm="4" :md="4" :lg="3" :xl="3">
                    <el-button icon="el-icon-caret-top" type="text">赞</el-button>
                    <span class="hidden-md-and-down">: {{ item.likeNum }} </span>
                  </el-col>
                  <el-col :span="3" :xs="4" :sm="4" :md="4" :lg="3" :xl="3">
                    <el-button icon="el-icon-caret-bottom" type="text">踩</el-button>
                    <span class="hidden-md-and-down">: {{ item.dislikeNum }} </span>
                  </el-col>
                  <el-col :span="3" :xs="4" :sm="4" :md="4" :lg="3" :xl="3">
                    <el-button icon="el-icon-plus" type="text" @click="item.addreply=true">回复</el-button>
                  </el-col>
                </el-row>
              </el-header>
              <el-main class="indis-container">
                <el-row v-for="initem in item.indiscussion" :key="initem.id">
                  <el-col :span="8">
                    {{ initem.userName }}
                    <div style="display:inline" v-if="initem.userType">&nbsp;&nbsp;V</div>
                  </el-col>
                  <el-col>
                    <div>:{{ initem.indisMessage }}</div>
                  </el-col>
                  <el-col>
                    <br />
                  </el-col>
                </el-row>
                <el-row v-if="item.addreply">
                  <div class="write-reply">
                    <el-input
                      type="textarea"
                      :rows="4"
                      placeholder="请输入内容"
                      v-model="item.replyMsg">
                    </el-input>
                  </div>
                  <div class="reply-btn">
                    <el-button type="primary" icon="el-icon-edit" @click="item.addreply=false">发表</el-button>
                    <el-button icon="el-icon-delete" @click="item.replyMsg=''">清空</el-button>
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
          :total="totalnumber"
          :current-page.sync="pageNo"
          :pager-count="7"
          @current-change="flipeOver"
        >
        </el-pagination>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  data: function() {
    var phoneReg = /^1[3|4|5|7|8][0-9]\d{8}$/
    var validateloPhone = (rule, value, callback) => {
      if (!this.loform.phonenumber) {
        return callback(new Error('号码不能为空'))
      }
      setTimeout(() => {
        if (!phoneReg.test(this.loform.phonenumber)) {
          callback(new Error('格式有误'))
        } else {
          callback()
        }
      }, 100)
    }
    return {
      login: true,
      loginFormVisible: false,
      loginLabelWidth: '100px',
      loform: {
        phonenumber: '',
        password: '',
        delivery: false,
        usercode: ''
      },
      rules: {
        lophone: [{ required: true, validator: validateloPhone, trigger: 'blur' }]
      },
      coursePic: require('../../assets/images/free.jpg'),
      playTime: 0,
      courseaudio: require('../../assets/audios/audio1.mp3'),
      music: {
        isPlay: false,
        currentTime: 0,
        maxTime: 0,
        volume: 100
      },
      courseid: '',
      course_artical: '在十九课里，我们学到了赵州桥是多么的雄伟、壮观。想一想，以前的桥就让我们赞不绝口，未来的桥会是怎样的呢？开动你的小脑筋，仔细想一想吧在未来的世界里，桥是透明的，看不见，摸得着。一辆辆车以最快的速度冲向桥，都想争夺第一个飞马王子。原来啊，由于桥是透明的，看不见桥，只能看见一辆辆在桥上飞奔的汽车，所以就像车在天上飞一样。在桥上的人和汽车，既能看见远处的风景，让自己欣赏，又能让别人看了以为是在天上飞的汽车，让他们赞叹不已。这就是未来的桥，一个桥上的创举。在十九课里，我们学到了赵州桥是多么的雄伟、壮观。想一想，以前的桥就让我们赞不绝口，未来的桥会是怎样的呢？开动你的小脑筋，仔细想一想吧在未来的世界里，桥是透明的，看不见，摸得着。一辆辆车以最快的速度冲向桥，都想争夺第一个飞马王子。原来啊，由于桥是透明的，看不见桥，只能看见一辆辆在桥上飞奔的汽车，所以就像车在天上飞一样。在桥上的人和汽车，既能看见远处的风景，让自己欣赏，又能让别人看了以为是在天上飞的汽车，让他们赞叹不已。这就是未来的桥，一个桥上的创举。',
      config: {
        // url: '', // 网址，默认使用 window.location.href
        source: '', // 来源（QQ空间会用到）, 默认读取head标签
        title: '', // 标题，默认读取 document.title 或者 <meta name="title" content="share.js" />
        description: '', // 描述, 默认读取head标签
        image: '', // 图片, 默认取网页中第一个img标签
        sites: ['qzone', 'qq', 'weibo', 'wechat'], // 启用的站点
        wechatQrcodeTitle: '微信扫一扫：分享', // 微信二维码提示文字
        wechatQrcodeHelper: '<p>微信里点“发现”，扫一下</p><p>二维码便可将本文分享至朋友圈。</p>'
        // disabled: ['google', 'facebook', 'twitter'], // 禁用的站点
      },
      discussWord: '',
      discussionList: [
        {
          userName: 'gyy',
          userImg: require('../../assets/images/userImg.jpg'),
          userType: false,
          discussTime: '2018.8.22 19:00',
          discussMessage: '啦啦啦啦啦啦啦啦啦啦',
          likeNum: 0,
          dislikeNum: 0,
          addreply: false,
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
          addreply: false,
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
      totalnumber: 100,
      pageNo: 1
    }
  },
  methods: {
    logout() {
      this.login = false
    },
    formatTime(val) {
      return val / 100 * this.music.maxTime
    },
    formatVoice(val) {
      return val
    },
    flipeOver: function (page) {
      let _end = this.pageSize * page
      let end = this.totalnumber < (_end) ? this.totalnumber : _end
      this.freeList = []
      let start = this.pageSize * (page - 1)
      for (let i = start; i < end; i++) {
        this.freeList.push(this.courses[i])
      }
    }
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
  .coursePic {
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
    margin: auto auto 10px auto;
    text-align: center;
    vertical-align: middle;
  }
  .el-icon-caret-right::before {
    font-size: 25px;
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
  }
  .share-container {
    width: 900px;
    margin: 80px auto 150px auto;
    text-align: right;
  }
  .discuss-container {
    width: 1200px;
    max-height: 2500px;
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

  @media screen and (max-width: 500px) {
    .user-ope {
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
