<template>
  <div id="body">
    <div class="toolbar">
      <div class="logo">
      <img src="../../assets/logo1.png" width="200%" height="100%">
      </div>
      <table align="right">
        <tr>
          <td>
            <el-button class="user-ope" type="text" v-if="!login" @click="loginFormVisible = true">登录/注册</el-button>
          </td>
          <td>
            <router-link to="/personal">
              <el-button class="user-ope" type="text" v-if="login">个人中心</el-button>
            </router-link>
          </td>
          <td>
            <el-button class="user-ope" type="text" v-if="login" @click="logout">登出</el-button>
          </td>
        </tr>
      </table>
    </div>

    <div class="logindialog">
      <el-dialog title="登录" :visible.sync="loginFormVisible" width="400px" height="700px">
        <el-form :model="loform" :rules="rules">
          <el-form-item label="手机号" label-width="100px" prop="lophone">
            <el-col :span="18">
              <el-input v-model="loform.phonenumber" auto-complete="true" clearable required="required" pattern="/^1[3|4|5|7|8][0-9]\d{8}$/" oninvalid="this.setCustomValidity('warning')"></el-input>
            </el-col>
          </el-form-item>
          <el-form-item label="验证码" label-width=100px>
            <el-col :span="18">
              <el-input v-model="loform.password" auto-complete="off" clearable></el-input>
            </el-col>
          </el-form-item>
        </el-form>
        <div slot="footer" class="login-footer">
          <el-button type="primary" @click="loginFormVisible = false">获取验证码</el-button>
          <el-button @click="loginFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="loginFormVisible = false">确 定</el-button>
        </div>
      </el-dialog>
    </div>

    <div >
      <el-card class="box-card" shadow="always">
        <div slot="header" class="clear-fix">
          <img alt="" :src="picture" width="100%" height="250px"/>
        </div>
        <div class="title-div">
          <el-container>
            <el-aside>
              <div id="class">
                课程:{{ title }}
              </div>
            </el-aside>
            <el-main>
              <div class="operate">
                <el-button
                  class="judge-button"
                  type="primary"
                  v-if = "!login"
                  @click="loginFormVisible = true">立即观看
                </el-button>
                <el-button
                  class="judge-button"
                  type="danger"
                  plain v-else-if = "burnedFlag"
                  @click="fire">已焚毁
                </el-button>
                <el-button
                  class="judge-button"
                  type="primary"
                  size="small"
                  round
                  v-else-if = "paidFlag || !moneyFlag"
                  @click="toCourse">立即观看
                </el-button>
                <el-button
                  class="judge-button"
                  type="primary"
                  v-else-if = "paidFlag==0"
                  @click="payDialogVisible = true"
                  width="120px"
                  height="50px">￥{{ money }}购买
                </el-button>
              </div>
            </el-main>
          </el-container>
        </div>
        <div>
          <p class="class-content" align="justify">{{ classIntro }}</p>
        </div>
        <div class="share-div">
          <i class="el-icon-share"></i>
          <share :config="config" class="share"></share>
        </div>
      </el-card>
    </div>
    <div class = "pay-dialog">
      <el-dialog
        title="支付"
        :visible.sync="payDialogVisible"
        width="500px"
        height="400px">
        <div class="pay-head">
          <div id="pay-money">课程:{{ title }}</div>
          <div id="pay-dialog-money">￥{{ money }}</div>
        </div>
        <div class="hint">现金支付</div>
        <div class="pay-frame">
          <el-radio v-model="channel" label="alipay_qr">支付宝支付</el-radio>
          <el-radio v-model="channel" label="wx_pub_qr">微信支付</el-radio>
        </div>
        <el-button
          class="pay"
          type="primary"
          @click="payWithCash">立即支付
        </el-button>
        <div class="hint">赏金支付</div>
        <el-button
          class="pay"
          type="primary"
          v-if ="bountyFlag">赏金支付
        </el-button>
        <el-button
          class="pay"
          type="primary"
          plain v-else disabled>赏金不足
        </el-button>
        <span id="account">当前赏金:{{ bounty }}</span>
      </el-dialog>
    </div>

    <br />
    <el-footer height="50px" class="hidden-lg-and-down"></el-footer>

  </div>
</template>

<script>
import axios from 'axios'
import qs from 'qs'
import * as utils from '../utils/utils.js'

export default {
  data() {
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
      user: '0',
      courseid: '',
      sharePerson: '',
      title: '我们爱科学',
      buttonShow: '观看',
      // burnedFlag表示当前是否焚毁（true为已焚毁）
      burnedFlag: false,
      // money表示当前课程的价钱，moneyFlag表示该课是否免费（true为付费 false为免费）
      moneyFlag: true,
      money: '25',
      // paidFlag表示当前用户是否已支付该课程(true 表示已支付)
      paidFlag: true,
      classIntro: '这就是未来的桥，一个桥上的创举。',
      picture: require('../../assets/class3.jpg'),
      payDialogVisible: false,
      bounty: 15,
      bountyFlag: false,
      shareDialogVisible: false,
      login: true,
      loginLabelWidth: '100px',
      loginFormVisible: false,
      loform: {
        phonenumber: '',
        password: '',
        delivery: false,
        type: [],
        resource: '',
        desc: ''
      },
      rules: {
        lophone: [
          {
            required: true,
            validator: validateloPhone,
            trigger: 'blur'
          }
        ]
      },
      channel: '',
      config: {
        url: '', // 网址，默认使用 window.location.href
        // source: '', // 来源（QQ空间会用到）, 默认读取head标签
        // title: '', // 标题，默认读取 document.title 或者 <meta name="title" content="share.js" />
        // description: '', // 描述, 默认读取head标签
        // image: '', // 图片, 默认取网页中第一个img标签
        sites: ['qzone', 'qq', 'weibo', 'wechat'] // 启用的站点
        // wechatQrcodeTitle: '微信扫一扫：分享', // 微信二维码提示文字
        // wechatQrcodeHelper: '<p>微信里点“发现”，扫一下</p><p>二维码便可将本文分享至朋友圈。</p>'
        // disabled: ['google', 'facebook', 'twitter'], // 禁用的站点
      }
    }
  },
  methods: {
    toCourse: function() {
      this.$router.push({path: '/coursepage/' +
        this.courseid + '/' + this.user})
    },
    payWithCash: function() {
      axios.post(utils.getURL() + 'api/paywithqr/', qs.stringify({
        channel: this.channel,
        amount: this.money,
        course_name: this.title,
        sharer: this.shareperson
      })).then(response => {
        let status = response.data.status
        if (status === 0) {
          window.open(response.data.result)
        }
      })
    },
    fire: function() {
      this.$router.push({ path: '/destroied' })
    }
  },
  created: function() {
    this.courseid = this.$route.params.courseid
    this.sharePerson = this.$route.params.user
    this.user = this.$route.params.user
    // 以下一行放到登录函数里
    this.config.url = utils.getURL() +
      '#/intro/' + this.courseid + '/' + this.user
    axios.post(utils.getURL() + 'api/getcourseinfo/', qs.stringify({
      course_id: this.courseid
    })).then(response => {
      let data = response.data
      this.title = data.title
      this.classIntro = data.description
      this.money = parseFloat(data.price)
      if (this.money > 0) {
        this.moneyFlag = true
      } else {
        this.moneyFlag = false
      }
    })
  }
}
</script>
<style scoped>
  .el-main {
    padding: 0px;
  }
  .box-card {
    max-width: 1000px;
    max-height: 800px !important;
    margin: 20px auto;
    text-align: center;
  }
  .toolbar {
    width: 100%;
    max-height: 50px;
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

  #class {
    font-family: "Arial","Microsoft YaHei","黑体","宋体",sans-serif;
    font-size: 24px;
    font-weight: bold;
    text-align: left;
  }

  .money {
    color: red ;
    font-size: 20px;
    font-weight: bold;
    text-align: left;
    letter-spacing: 0;
    padding-bottom: 20px;
  }

  .picturebox {
    width: 600px;
    height: 400px;
  }

  #page {
    max-width: 600px;
    margin:0px auto 0px auto;
    padding:40px;
    border-left-style: solid;
    border-left-width: 1px;
    border-right-style: solid;
    border-right-width: 1px;
    border-bottom-style: solid;
    border-bottom-width: 1px;
    border-top-style: solid;
    border-top-width: 1px;
  }

  .class-content {
    text-indent: 2em;
    margin-bottom: 20px;
    margin-top: 20px;
    letter-spacing: 0.2em;
    font-size: 14px;
  }

  .el-icon-share {
    width: 20px;
    height:30px;
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

  .pay {
    margin:20px;
    margin-left: 50px;
    margin-top: 0px;
    margin-bottom: 60px;
    width: 100px;
  }

  .el-dialog__body {
    padding-top: 20px;
  }

  #pay-money {
    font-size: 22px;
    margin-bottom: 20px;
    margin-left: 50px;
    margin-top: 0px;
    font-weight: bold;
  }

  #pay-dialog-money {
    font-size: 22px;
    margin-bottom: 20px;
    margin-left: 50px;
    margin-top: 0px;
    font-weight: bold;
    color: red;
  }

  .hint {
    margin-left: 50px;
    margin-bottom: 40px;
    font-size: 18px;
    font-weight: bolder;
  }

  .pay-head {
    margin-bottom: 60px;
  }

  .pay-frame {
    margin-left: 50px;
    margin-bottom: 30px;
  }

  #account {
    margin-left: 0px;
    font-size: 15px;
    color:#409EFF;
  }

  #sharetext {
    font-size: 24px;
    font-weight: bold;
    margin: 20px;
  }

  .share {
    margin: 20px;
    width: 150px;
    height: 45px;
  }

  .operate {
    text-align: right;
  }

  .share-div {
    text-align: right;
  }
  .share {
    display: inline;
  }
  @media screen and (max-width: 500px) {
    .user-ope {
      color: black;
      font-size:15px;
      margin-right: 10px;
    }
    .el-aside {
      width: 50% !important;
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
    .picturebox {
      width: 100%;
      height: 10%;
    }
    #class {
      font-family: "Arial","Microsoft YaHei","黑体","宋体",sans-serif;
      font-size: 18px;
      font-weight: bold;
      padding-bottom: 10px;
      padding-top: 10px;
    }
    .money {
      color: red ;
      font-size: 18px;
      font-weight: bold;
      letter-spacing: 0;
      padding-bottom: 10px;
    }
    .class-content {
      text-indent: 2em;
      margin-bottom: 40px;
      letter-spacing: 0.2em;
      font-size: 14px;
    }
  }
</style>
