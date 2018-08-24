<!-- Add "scoped" attribute to limit CSS to this component only -->
<template>
  <div class="index">
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

    <div class="carousel">
      <el-carousel :interval="4000" type="card">
        <el-carousel-item v-for="item in imgList" :key="item.id">
            <router-link id="logo" :to="{name:'intro',params:{courseid: item.id}}">
              <el-col :span="24"><img height="100%" width="100%" :src="item.profile_url" class="banner_img"/></el-col>
            </router-link>
        </el-carousel-item>
      </el-carousel>
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
          <el-button type="primary" @click="getVerification">获取验证码</el-button>
          <el-button @click="loginFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="loginFunction">确 定</el-button>
        </div>
      </el-dialog>
    </div>

    <div class="hidden-md-and-down">&nbsp;</div>
    <hr />
    <div class="hidden-md-and-down">&nbsp;</div>
    <div class="free-list">
      <el-row :gutter="30" class="hidden-md-and-down">
        <el-col :span="8">
          <h1 style="text-align:left;">免费区</h1>
        </el-col>
        <el-col :span="4" :offset="11">
          <router-link to="/freelistpage">
            <el-button class="morelist" type="text">更多<i class="el-icon-more el-icon--right"></i></el-button>
          </router-link>
        </el-col>
      </el-row>
      <el-row class="hidden-lg-and-up">
        <el-col :span="8">
          <h3 style="text-align:left;">免费区</h3>
        </el-col>
        <el-col :span="4" :offset="11">
          <router-link to="/freelistpage">
            <el-button class="phonemorelist" type="text">更多<i class="el-icon-more el-icon--right"></i></el-button>
          </router-link>
        </el-col>
      </el-row>
      <el-row>
        <div>&nbsp;</div>
      </el-row>
      <el-row :gutter="30">
        <el-col v-for="item in freeList_1" :key="item.id" :span="8">
          <router-link id="logo" :to="{name:'intro',params:{courseid: item.id}}">
            <img :src="item.profile_url" class="recomimg" >
            <div style="display:inline word-break:break-all word-wrap:break-word">{{item.name}}</div>
          </router-link>
        </el-col>
      </el-row>
      <el-row :gutter="30">
        <el-col v-for="item in freeList_2" :key="item.id" :span="8">
          <router-link id="logo" :to="{name:'intro',params:{courseid: item.id}}">
            <img :src="item.profile_url" class="recomimg">
            <div style="display:inline word-break:break-all word-wrap:break-word">{{item.name}}</div>
          </router-link>
        </el-col>

      </el-row>
    </div>

    <div class="hidden-md-and-down">&nbsp;</div>
    <hr />
    <div class="hidden-md-and-down">&nbsp;</div>

    <div class="cost-list">
      <el-row :gutter="20" class="hidden-md-and-down">
        <el-col :span="8">
          <h1 style="text-align:left;">付费区</h1>
        </el-col>
        <el-col :span="4" :offset="11">
          <router-link to="/freelistpage">
            <el-button class="morelist" type="text">更多<i class="el-icon-more el-icon--right"></i></el-button>
          </router-link>
        </el-col>
      </el-row>
      <el-row class="hidden-lg-and-up">
        <el-col :span="8">
          <h3 style="text-align:left;">付费区</h3>
        </el-col>
        <el-col :span="4" :offset="11">
          <router-link to="/costlistpage">
            <el-button class="phonemorelist" type="text">更多<i class="el-icon-more el-icon--right"></i></el-button>
          </router-link>
        </el-col>
      </el-row>
      <el-row>
        <div>&nbsp;</div>
      </el-row>
      <el-row :gutter="20">
        <el-col v-for="item in costList_1" :key="item.id" :span="8">
          <router-link id="logo" :to="{name:'intro',params:{courseid: item.id}}">
            <img :src="item.profile_url" class="recomimg">
            <div style="display:inline word-break:break-all word-wrap:break-word">{{item.name}}</div>
          </router-link>
        </el-col>
      </el-row>
      <el-row :gutter="20">
        <el-col v-for="item in costList_2" :key="item.id" :span="8">
          <router-link id="logo" :to="{name:'intro',params:{courseid: item.id}}">
            <img :src="item.profile_url" class="recomimg">
            <div style="display:inline word-break:break-all word-wrap:break-word">{{item.name}}</div>
          </router-link>
        </el-col>
      </el-row>
    </div>
    <br />
    <br />
    <br />
    <el-footer height="50px" class="hidden-lg-and-down">2100实验室 联系电话：010-86398756 关注我们：微信服务号：科学队长</el-footer>

  </div>
</template>

<script>
import axios from 'axios'
import qs from 'qs'
import * as utils from '../utils/utils.js'

export default {
  data: function () {
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
      imgList: [
        {id: 0, profile_url: require('../../assets/images/banner1.jpg')},
        {id: 1, profile_url: require('../../assets/images/banner1.jpg')},
        {id: 2, profile_url: require('../../assets/images/banner1.jpg')}
      ],
      freeList_1: [
        {id: 0, profile_url: require('../../assets/images/free.jpg'), name: '啊啊啊啊啊'},
        {id: 1, profile_url: require('../../assets/images/free.jpg'), name: '啊啊啊啊啊'},
        {id: 2, profile_url: require('../../assets/images/free.jpg'), name: '啊啊啊啊啊'}
      ],
      freeList_2: [
        {id: 3, profile_url: require('../../assets/images/free.jpg'), name: '呜呜呜呜呜呜呜呜'},
        {id: 4, profile_url: require('../../assets/images/free.jpg'), name: '呜呜呜呜呜呜呜呜'},
        {id: 5, profile_url: require('../../assets/images/free.jpg'), name: '啊啊啊啊啊'}
      ],
      costList_1: [
        {id: 6, profile_url: require('../../assets/images/paid.jpg'), name: '喵喵喵喵喵'},
        {id: 7, profile_url: require('../../assets/images/paid.jpg'), name: '喵喵喵喵喵'},
        {id: 8, profile_url: require('../../assets/images/paid.jpg'), name: '喵喵喵喵喵'}
      ],
      costList_2: [
        {id: 9, profile_url: require('../../assets/images/paid.jpg'), name: '喵喵喵喵喵'},
        {id: 10, profile_url: require('../../assets/images/paid.jpg'), name: '喵喵喵喵喵'},
        {id: 11, profile_url: require('../../assets/images/paid.jpg'), name: '喵喵喵喵喵'}
      ],
      login: false,
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
      }
    }
  },
  methods: {
    createRandom: function() {
      var code = Math.floor(Math.random() * (99999 - 0) + 100000)
      this.loform.password = code.toString()
    },
    loginFunction: function() {
      if (this.loform.delivery === false) {
        alert('请输入正确的手机号和对应的验证码！')
        return
      }
      if (this.loform.usercode !== this.loform.password) {
        alert('请输入正确的验证码！')
        return
      }
      this.loginFormVisible = false
      axios.post(utils.getURL() + 'api/authenticate/', qs.stringify({
        phone_number: this.loform.phonenumber,
        verification_code: 0
      })).then(
        response => {
          this.login = true
          //  = response.data.user.alias
          //  = response.data.user.icon
        }
      )
    },
    getVerification: function() {
      if (this.loform.phonenumber === '') {
        alert('请输入正确的手机号！')
        return
      }
      this.createRandom()
      axios.post(utils.getURL() + 'api/getcode/', qs.stringify({
        phone_number: this.loform.phonenumber,
        password: this.loform.password
      })).then(
        response => {
          this.loform.delivery = true
        }
      )
    },
    logout: function() {
      axios.post(utils.getURL() + 'api/logout/').then(response => {
        this.login = false
      })
    }
  },
  created: function () {
    axios.post(utils.getURL() + 'api/login/').then(response => {
      this.login = response.data.status
    })
    axios.post(utils.getURL() + 'api/listrecommend/').then(response => {
      this.imgList = response.data.courses
    })
    axios.post(utils.getURL() + 'api/listfreeindex/').then(response => {
      let list = response.data.courses
      let length = list.length
      this.freeList_1 = []
      this.freeList_2 = []
      if (length > 3) {
        for (let i = 0; i < 3; i++) {
          this.freeList_1.push(list[i])
        }
        for (let i = 3; i < length; i++) {
          this.freeList_2.push(list[i])
        }
      } else {
        this.freeList_1 = list
      }
    })
    axios.post(utils.getURL() + 'api/listpricedindex/').then(response => {
      let list = response.data.courses
      let length = list.length
      this.costList_1 = []
      this.costList_2 = []
      if (length > 3) {
        for (let i = 0; i < 3; i++) {
          this.costList_1.push(list[i])
        }
        for (let i = 3; i < length; i++) {
          this.costList_2.push(list[i])
        }
      } else {
        this.costList_1 = list
      }
    })
  }
}
</script>

<style scoped>
  body {
    margin:0 auto;
  }
  #app {
    margin: 0;
    padding: 0;
  }

  .index {
    margin: 0 auto;
  }

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
  .carousel {
    max-width: 1200px;
    text-align: center;
    margin: 20px auto;
  }
  .banner_img {
    height: 100%;
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
  .free-list {
    max-width:1200px;
    margin:20px auto 20px auto;
  }
  .cost-list {
    max-width:1200px;
    margin:20px auto 20px auto;
  }
  .morelist {
    width: 100%;
    height: 100%;
    border: 2px, solid, black;
    border-radius: 5px;
    font-size: 30px;
    color: grey;
  }
  .morelist:hover {
    background-color:rgb(240, 240, 240);
    opacity: 0.7;
    color:black;
  }
  .phonemorelist {
    width: 100%;
    height: 100%;
    border: 2px, solid, black;
    border-radius: 5px;
    font-size: 18px;
    color: black;
  }
  hr {
    max-width: 1200px;
  }
  .recomimg {
    width: 90%;
    height: 80%
  }
  @media screen and (max-width: 500px) {
    .el-carousel {
      max-width: 1200px;
      max-height: 160px;
    }
    .el-carousel__container {
      max-width: 1200px;
      max-height: 140px;
    }
    .el-carousel__item {
      max-height: 120px
    }
    .user-ope {
      color:#085078;
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
  .el-carousel__container {
      max-width: 1200px;
      height: 350px;
  }
  .el-carousel__item {
    max-height: 350px;
  }
</style>
