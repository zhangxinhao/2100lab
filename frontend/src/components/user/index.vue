<!-- Add "scoped" attribute to limit CSS to this component only -->
<template>
  <div class="index">
    <div class="toolbar">
      <div class="logo">
        <img src="../../assets/logo3.png" width="200%" height="80%">
      </div>
      <table align="right">
        <tr>
          <td>
            <el-button class="user-ope" v-if="!login" @click="loginFormVisible = true" type="text">登录</el-button>
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
            <router-link id="logo" :to="{name:'intro',params:{courseid: item.id, user: user}}">
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
        <el-button type="text" class="getcheck" @click="getVerification">获取验证码</el-button>
        <div slot="footer" class="login-footer">
          <el-button @click="loginFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="loginFunction">确 定</el-button>
        </div>
      </el-dialog>
    </div>

    <div class="hidden-md-and-down"><br></div>
    <hr />
    <div class="hidden-md-and-down"><br></div>
    <div class="free-list">
      <el-row :gutter="30" class="hidden-md-and-down">
        <el-col :span="8">
          <h1>免费区</h1>
        </el-col>
        <el-col :span="4" :offset="11">
          <router-link to="/freelistpage">
            <el-button class="morelist" type="text">更多
              <i class="el-icon-more el-icon--right"></i>
            </el-button>
          </router-link>
        </el-col>
      </el-row>
      <el-row class="hidden-lg-and-up">
        <el-col :span="8">
          <h3>免费区</h3>
        </el-col>
        <el-col :span="4" :offset="11">
          <router-link to="/freelistpage">
            <el-button class="phonemorelist" type="text">更多
              <i class="el-icon-more el-icon--right"></i>
            </el-button>
          </router-link>
        </el-col>
      </el-row>
      <el-row>
      <br/>
      </el-row>
      <el-row :gutter="30" class="hidden-md-and-down" type="flex" justify="center" id="free1">
        <el-col :span="6" v-for="item in freeList_1" :key="item.id" :offset="item.id > 0 ? 2 : 0">
          <el-card :body-style="{ padding: '0px' }" class="card-one">
            <img :src="item.profile_url" class="recomimg">
            <div style="padding: 14px;">
              <span>{{ item.name }}</span>
              <div class="bottom clearfix">
                <router-link id="logo" :to="{name:'intro',params:{courseid: item.id, user: user}}">
                  <el-button type="text" class="button">点击观看</el-button>
                </router-link>
              </div>
            </div>
          </el-card>
        </el-col>
      </el-row>
      <div class="hidden-lg-and-up">
        <div class="video-list">
          <ul class="vd-list">
            <li v-for="item in freeList_1" :key="item.id" class="list-one">
              <el-container class="list-one-outer">
                <el-aside class="aside">
                  <router-link
                    id="logo"
                    :to="{name:'intro',params:{courseid: item.id}}">
                    <img
                      :src="item.profile_url"
                      :alt="item.name"
                      class="img-list">
                  </router-link>
                </el-aside>
                <el-container class="list-one-inner">
                  <el-header class="header">
                    <div>{{item.name}}</div>
                  </el-header>
                  <el-main class="main">
                    <el-button
                      icon="el-icon-caret-right"
                      type="primary"
                      class="read">点击阅读
                    </el-button>
                  </el-main>
                </el-container>
              </el-container>
              <hr />
            </li>
          </ul>
        </div>
      </div>

      <el-row :gutter="30" class="hidden-md-and-down" type="flex" justify="center" id="free2">
        <el-col :span="6" v-for="item in freeList_2" :key="item.id" :offset="item.id > 3 ? 2 : 0">
          <el-card :body-style="{ padding: '0px' }" class="card-one">
            <img :src="item.profile_url" class="recomimg">
            <div style="padding: 14px;">
              <span>{{ item.name }}</span>
              <div class="bottom clearfix">
                <router-link id="logo" :to="{name:'intro',params:{courseid: item.id, user: user}}">
                  <el-button type="text" class="button">点击观看</el-button>
                </router-link>
              </div>
            </div>
          </el-card>
        </el-col>
      </el-row>

    </div>

    <div class="hidden-md-and-down"><br></div>
    <hr class="hidden-md-and-down" />
    <div class="hidden-md-and-down"><br></div>

    <div class="cost-list">
      <el-row :gutter="20" class="hidden-md-and-down">
        <el-col :span="8">
          <h1>付费区</h1>
        </el-col>
        <el-col :span="4" :offset="11">
          <router-link to="/freelistpage">
            <el-button class="morelist" type="text">更多
              <i class="el-icon-more el-icon--right"></i>
            </el-button>
          </router-link>
        </el-col>
      </el-row>
      <el-row class="hidden-lg-and-up">
        <el-col :span="8">
          <h3>付费区</h3>
        </el-col>
        <el-col :span="4" :offset="11">
          <router-link to="/costlistpage">
            <el-button class="phonemorelist" type="text">更多
              <i class="el-icon-more el-icon--right"></i>
            </el-button>
          </router-link>
        </el-col>
      </el-row>
      <el-row>
      <br>
      </el-row>
      <el-row :gutter="30" class="hidden-md-and-down" type="flex" justify="center" id="cost1">
        <el-col :span="6" v-for="item in costList_1" :key="item.id" :offset="item.id > 6 ? 2 : 0">
          <el-card :body-style="{ padding: '0px' }" class="card-one">
            <img :src="item.profile_url" class="recomimg">
            <div style="padding: 14px;">
              <span>{{ item.name }}</span>
              <div class="bottom clearfix">
                <router-link id="logo" :to="{name:'intro',params:{courseid: item.id, user: user}}">
                  <el-button type="text" class="button">点击观看</el-button>
                </router-link>
              </div>
            </div>
          </el-card>
        </el-col>
      </el-row>

      <div class="hidden-lg-and-up">
        <div class="video-list">
          <ul class="vd-list">
            <li v-for="item in costList_1" :key="item.id" class="list-one">
              <el-container class="list-one-outer">
                <el-aside class="aside">
                  <router-link
                    id="logo"
                    :to="{name:'intro',params:{courseid: item.id}}">
                    <img
                      :src="item.profile_url"
                      :alt="item.name"
                      class="img-list">
                  </router-link>
                </el-aside>
                <el-container class="list-one-inner">
                  <el-header class="header">
                    <div>{{item.name}}</div>
                  </el-header>
                  <el-main class="main">
                    <el-button
                      icon="el-icon-caret-right"
                      type="primary"
                      class="read">点击阅读
                    </el-button>
                  </el-main>
                </el-container>
              </el-container>
              <hr />
            </li>
          </ul>
        </div>
      </div>

      <el-row :gutter="30" class="hidden-md-and-down" type="flex" justify="center" id="cost2">
        <el-col :span="6" v-for="item in costList_2" :key="item.id" :offset="item.id > 9 ? 2 : 0">
          <el-card :body-style="{ padding: '0px' }" class="card-one">
            <img :src="item.profile_url" class="recomimg">
            <div style="padding: 14px;">
              <span>{{ item.name }}</span>
              <div class="bottom clearfix">
                <router-link id="logo" :to="{name:'intro',params:{courseid: item.id, user: user}}">
                  <el-button type="text" class="button">点击观看</el-button>
                </router-link>
              </div>
            </div>
          </el-card>
        </el-col>
      </el-row>
    </div>
    <br />
    <br />
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
      user: '0',
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
      let length = response.data.courses.length
      for (let i = 0; i < length; i++) {
        this.imgList[i].id = response.data.courses[i].id
        this.imgList[i].profile_url = utils.getURL() + 'media/' +
          response.data.courses[i].profile_url
      }
    })
    axios.post(utils.getURL() + 'api/listfreeindex/').then(response => {
      let list = response.data.courses
      let length = list.length
      let course = {
        id: '',
        profile_url: '',
        name: ''
      }
      this.freeList_1 = []
      this.freeList_2 = []
      if (length > 3) {
        for (let i = 0; i < 3; i++) {
          course.id = list[i].pk
          course.profile_url = utils.getURL() + 'media/' +
            list[i].fields.profile_url
          course.name = list[i].fields.course_name
          this.freeList_1.push(course)
        }
        for (let i = 3; i < length; i++) {
          course.id = list[i].pk
          course.profile_url = utils.getURL() + 'media/' +
            list[i].fields.profile_url
          course.name = list[i].fields.course_name
          this.freeList_2.push(course)
        }
      } else {
        for (let i = 0; i < length; i++) {
          course.id = list[i].pk
          course.profile_url = utils.getURL() + 'media/' +
            list[i].fields.profile_url
          course.name = list[i].fields.course_name
          this.freeList_1.push(course)
        }
      }
    })
    axios.post(utils.getURL() + 'api/listpricedindex/').then(response => {
      let list = response.data.courses
      let length = list.length
      let course = {
        id: '',
        profile_url: '',
        name: ''
      }
      this.costList_1 = []
      this.costList_2 = []
      if (length > 3) {
        for (let i = 0; i < 3; i++) {
          course.id = list[i].pk
          course.profile_url = utils.getURL() + 'media/' +
            list[i].fields.profile_url
          course.name = list[i].fields.course_name
          this.costList_1.push(course)
        }
        for (let i = 3; i < length; i++) {
          course.id = list[i].pk
          course.profile_url = utils.getURL() + 'media/' +
            list[i].fields.profile_url
          course.name = list[i].fields.course_name
          this.costList_2.push(course)
        }
      } else {
        for (let i = 0; i < length; i++) {
          course.id = list[i].pk
          course.profile_url = utils.getURL() + 'media/' +
            list[i].fields.profile_url
          course.name = list[i].fields.course_name
          this.costList_1.push(course)
        }
      }
    })
  }
}
</script>

<style scoped>
  .index {
    background-color: rgb(240, 240, 240);
  }
  .toolbar {
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
  .carousel {
    max-width: 1200px;
    text-align: center;
    margin: 20px auto;
  }
  .banner_img {
    height: 100%;
  }
  #footer {
    color: #333;
    text-align: center;
    line-height: 55px;
  }
  .free-list {
    max-width:1200px;
    margin:20px auto 20px auto;
  }
  .cost-list {
    max-width:1200px;
    margin:20px auto 20px auto;
  }
  .getcheck {
    margin-left: 100px !important;
  }
  .morelist {
    width: 100%;
    height: 100%;
    border-radius: 5px;
    font-size: 25px;
    color: grey;
  }
  .phonemorelist {
    width: 100%;
    height: 100%;
    border-radius: 5px;
    font-size: 18px;
    color: black;
  }
  hr {
    max-width: 1200px;
  }
  .recomimg {
    width: 100%;
    height: 200px;
  }
  h1, h3 {
    text-align: left;
  }
  .course-name {
    display: inline;
    word-break: break-all;
    word-wrap: break-word;
    font-size: 20px;
  }
  .button {
    padding: 0;
    float: right;
  }
  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }
  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }

  .clearfix:after {
    clear: both
  }
  .phone-recomimg {
    width: 80%;
  }
  #free1 {
    margin-bottom: 30px;
  }
  #cost1 {
    margin-bottom: 30px;
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
    .video-list {
      zoom: 1;
      margin-bottom: 20px;
      text-align: center;
    }
    .list-one-outer {
      max-width: 350px;
    }
    .list-one-inner {
      max-width: 200px;
    }
    .list-one {
      display: block;
      float: left;
      max-width: 350px;
      margin: 5px 0px;
    }
    .aside {
      max-width: 150px !important;
    }
    .img-list {
      max-width: 150px;
      height: 100px;
    }
    .header {
      max-width: 200px;
      height: 50px !important;
    }
    .main {
      max-width: 200px;
      height: 50px;
      padding: 10px;
      text-align: right;
    }
    .read {
      padding: 5px;
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
