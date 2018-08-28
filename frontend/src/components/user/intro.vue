<template>
  <div class="intro">
    <div id="body">
      <div class="tool-bar">
        <router-link to="/">
          <div class="logo">
            <img src="../../assets/logo3.png" width="200%" height="80%">
          </div>
        </router-link>
        <table align="right">
          <tr>
            <td>
              <el-button
                class="user-ope"
                type="text"
                v-if="!login"
                @click="loginFormVisible = true">
                登录
              </el-button>
            </td>
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
          width="400px"
          height="700px">
          <el-form :model="loform" :rules="rules">
            <el-form-item label="手机号" label-width="100px" prop="lophone">
              <el-col :span="18">
                <el-input
                  v-model="loform.phonenumber"
                  auto-complete="true"
                  clearable
                  required="required"
                  pattern="/^1[3|4|5|7|8][0-9]\d{8}$/"
                  oninvalid="this.setCustomValidity('warning')">
                </el-input>
              </el-col>
            </el-form-item>
            <el-form-item label="验证码" label-width=100px>
              <el-col :span="18">
                <el-input
                  v-model="loform.password"
                  auto-complete="off"
                  clearable>
                </el-input>
              </el-col>
            </el-form-item>
          </el-form>
          <div slot="footer" class="login-footer">
            <el-button
              type="primary"
              @click="loginFormVisible = false">
              获取验证码
            </el-button>
            <el-button @click="loginFormVisible = false">
              取 消
            </el-button>
            <el-button
              type="primary"
              @click="loginFormVisible = false">
              确 定
            </el-button>
          </div>
        </el-dialog>
      </div>

      <div class="card-contain">
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
            <p class="class-content" align="justify">
              {{ classIntro }}
            </p>
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
            <el-radio v-model="channel" label="alipay">
              支付宝支付
            </el-radio>
            <el-radio v-model="channel" label="wx">
              微信支付
            </el-radio>
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
      <br />
      <div class="hidden-md-and-down" id="footer">
        <img src="../../assets/footer1.png" width=100%>
      </div>
    </div>
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
      courseId: '',
      sharePerson: '',
      title: '我们爱科学',
      buttonShow: '观看',
      // burnedFlag表示当前是否焚毁（true为已焚毁）
      burnedFlag: false,
      // money表示当前课程的价钱，moneyFlag表示该课是否免费
      moneyFlag: true,
      money: 25,
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
        sites: ['qzone', 'qq', 'weibo', 'wechat'] // 启用的站点
      }
    }
  },
  methods: {
    toCourse: function() {
      this.$router.push({path: '/coursepage/' +
        this.courseId + '/' + this.user})
    },
    isPC: function() {
      let userAgentInfo = navigator.userAgent
      let agents = ['Android', 'iPhone', 'SymbianOS',
        'Windows Phone', 'iPad', 'iPod']
      let flag = true
      for (let v = 0; v < agents.length; v++) {
        if (userAgentInfo.indexOf(agents[v]) > 0) {
          flag = false
          break
        }
      }
      return flag
    },
    payInfo: function() {
      let info = {}
      info.amount = this.price
      info.courseId = this.courseId
      info.sharer = this.sharePerson
      info.successUrl = window.location.href
      return info
    },
    alipayPC: function() {
      let pingpp = require('pingpp-js')
      axios.post(utils.getURL() + 'api/alipaypc/', qs.stringify({
        info: JSON.stringify(this.payInfo())
      })).then(response => {
        pingpp.setUrlReturnCallback(function (err, url) {
          if (err) {
            this.$message.error(err)
          }
          window.open(url)
        }, ['alipay_pc_direct'])

        pingpp.createPayment(response.data.pingppObject,
          function (result, err) {
            this.$message.error(err)
          })
      })
    },
    alipayPhone: function() {
      let pingpp = require('pingpp-js')
      axios.post(utils.getURL() + 'api/alipayphone/', qs.stringify({
        info: JSON.stringify(this.payInfo())
      })).then(response => {
        pingpp.createPayment(response.data.pingppObject,
          function (result, err) {
            this.$message.error(err)
          })
      })
    },
    wxPC: function() {
      axios.post(utils.getURL() + 'api/wxpc/', qs.stringify({
        info: JSON.stringify(this.payInfo())
      })).then(response => {
        if (response.data.status === 0) {
          window.open(response.data.qr)
        }
      })
    },
    wxPhone: function() {
      let pingpp = require('pingpp-js')
      axios.post(utils.getURL() + 'api/wxphone/', qs.stringify({
        info: JSON.stringify(this.payInfo())
      })).then(response => {
        pingpp.createPayment(response.data.pingppObject,
          function (result, err) {
            this.$message.error(err)
          })
      })
    },
    payWithCash: function() {
      if (this.isPC()) {
        if (this.channel === 'alipay') {
          this.alipayPC()
        } else {
          this.wxPC()
        }
      } else {
        if (this.channel === 'alipay') {
          this.alipayPhone()
        } else {
          this.wxPhone()
        }
      }
    },
    fire: function() {
      this.$router.push({ path: '/destroied' })
    }
  },
  created: function() {
    this.courseId = this.$route.params.courseid
    this.sharePerson = this.$route.params.user
    this.user = this.$route.params.user
    // 以下一行放到登录函数里
    this.config.url = utils.getURL() +
      '#/intro/' + this.courseId + '/' + this.user
    axios.post(utils.getURL() + 'api/getcourseinfo/', qs.stringify({
      courseId: this.courseId
    })).then(response => {
      this.picture = utils.getURL() + 'media/' +
        response.data.list[0].fields.profile_url
      this.title = response.data.list[0].fields.course_name
      this.classIntro = response.data.list[0].fields.description
      this.money = response.data.list[0].fields.price
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
  .intro {
    height: 100%;
    background-color: rgb(240, 240, 240);
  }
  .el-main {
    padding: 0px;
  }
  .box-card {
    max-width: 1000px;
    max-height: 800px !important;
    margin: 20px auto;
    text-align: center;
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

  .user-ope {
    color: white;
    font-size:18px;
    margin-right: 60px;
  }

  #class {
    font-family: "Arial","Microsoft YaHei","黑体";
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

  #footer {
    color: #333;
    text-align: center;
    line-height: 55px;
  }
  .card-contain {
    min-height: 500px;
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
      color: white;
      font-size:15px;
      margin-right: 10px;
    }
    .el-aside {
      width: 50% !important;
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

    #class {
      font-family: "Arial","Microsoft YaHei","黑体";
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
