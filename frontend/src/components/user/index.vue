<!-- Add "scoped" attribute to limit CSS to this component only -->
<template>
  <div class="index">
    <div class="tool-bar">
      <div class="logo">
        <route-link to="/">
          <img src="../../assets/logo3.png" width="200%" height="80%">
        </route-link>
      </div>
      <table align="right">
        <tr>
          <td>
            <el-button
              class="user-ope"
              v-if="!login"
              @click="loginFormVisible = true"
              type="text">
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

    <div class="carousel">
      <el-carousel :interval="4000" type="card">
        <el-carousel-item v-for="item in imgList" :key="item.id">
            <router-link
              id="logo"
              :to="{name:'intro',params:{courseid: item.id, user: user}}">
              <el-col :span="24">
                <img
                  height="100%"
                  width="100%"
                  :src="item.profileUrl"
                  class="banner_img"/>
              </el-col>
            </router-link>
        </el-carousel-item>
      </el-carousel>
    </div>

    <div class="login-dialog">
      <el-dialog
        title="登录"
        :visible.sync="loginFormVisible"
        class="lo-dialog"
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
          <el-form-item label="验证码" :label-width="loginLabelWidth">
            <el-col :span="18">
              <el-input
                v-model="loForm.usercode"
                auto-complete="off"
                clearable>
              </el-input>
            </el-col>
          </el-form-item>
        </el-form>
        <el-button
          type="text"
          class="get-check"
          @click="getVerification">
          获取验证码
        </el-button>
        <div slot="footer" class="login-footer">
          <el-button @click="loginFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="loginFunction">
            确 定
          </el-button>
        </div>
      </el-dialog>
    </div>

    <div class="hidden-sm-and-down"><br /></div>
    <hr />
    <div class="hidden-sm-and-down"><br /></div>
    <div class="free-list">
      <el-row :gutter="30" class="hidden-sm-and-down">
        <el-col :span="8">
          <h1>免费区</h1>
        </el-col>
        <el-col :span="4" :offset="11">
          <router-link to="/freelistpage">
            <el-button class="more-list" type="text">更多
              <i class="el-icon-more el-icon--right"></i>
            </el-button>
          </router-link>
        </el-col>
      </el-row>
      <el-row class="hidden-md-and-up">
        <el-col :span="8">
          <h3>免费区</h3>
        </el-col>
        <el-col :span="4" :offset="11">
          <router-link to="/freelistpage">
            <el-button class="phone-more-list" type="text">更多
              <i class="el-icon-more el-icon--right"></i>
            </el-button>
          </router-link>
        </el-col>
      </el-row>
      <el-row>
      <br/>
      </el-row>
      <el-row
        :gutter="30"
        class="hidden-sm-and-down"
        type="flex"
        justify="center"
        id="free1">
        <el-col
          :span="6"
          v-for="item in freeList1"
          :key="item.id"
          :offset="item.id > 0 ? 2 : 0">
          <el-card :body-style="{ padding: '0px' }" class="card-one">
            <img :src="item.profileUrl" class="recomimg">
            <div class="only-div">
              <span>{{ item.name }}</span>
              <div class="bottom clearfix">
                <router-link
                  id="logo"
                  :to="{name:'intro',params:{courseid: item.id, user: user}}">
                  <el-button type="text" class="button">点击观看</el-button>
                </router-link>
              </div>
            </div>
          </el-card>
        </el-col>
      </el-row>
      <div class="hidden-md-and-up">
        <div class="video-list">
          <ul class="vd-list">
            <li v-for="item in freeList1" :key="item.id" class="list-one">
              <el-container class="list-one-outer">
                <el-aside class="aside">
                  <router-link
                    id="logo"
                    :to="{name:'intro',params:{courseid: item.id, user: user}}">
                    <img
                      :src="item.profileUrl"
                      :alt="item.name"
                      class="img-list">
                  </router-link>
                </el-aside>
                <el-container class="list-one-inner">
                  <el-header class="header">
                    <div>{{ item.name }}</div>
                  </el-header>
                  <el-main class="main">
                    <router-link
                      id="logo"
                      :to="{name:'intro',params:{courseid: item.id, user: user}}">
                      <el-button
                        icon="el-icon-caret-right"
                        type="primary"
                        class="read">点击观看
                      </el-button>
                    </router-link>
                  </el-main>
                </el-container>
              </el-container>
              <hr />
            </li>
          </ul>
        </div>
      </div>

      <el-row
        :gutter="30"
        class="hidden-sm-and-down"
        type="flex"
        justify="center"
        id="free2">
        <el-col
          :span="6"
          v-for="item in freeList2"
          :key="item.id"
          :offset="item.id > 3 ? 2 : 0">
          <el-card :body-style="{ padding: '0px' }" class="card-one">
            <img :src="item.profileUrl" class="recomimg">
            <div class="only-div">
              <span>{{ item.name }}</span>
              <div class="bottom clearfix">
                <router-link
                  id="logo"
                  :to="{name:'intro',params:{courseid: item.id, user: user}}">
                  <el-button type="text" class="button">点击观看</el-button>
                </router-link>
              </div>
            </div>
          </el-card>
        </el-col>
      </el-row>

    </div>

    <div class="hidden-sm-and-down"><br></div>
    <hr class="hidden-sm-and-down" />
    <div class="hidden-sm-and-down"><br></div>

    <div class="cost-list">
      <el-row :gutter="20" class="hidden-sm-and-down">
        <el-col :span="8">
          <h1>付费区</h1>
        </el-col>
        <el-col :span="4" :offset="11">
          <router-link to="/costlistpage">
            <el-button class="more-list" type="text">更多
              <i class="el-icon-more el-icon--right"></i>
            </el-button>
          </router-link>
        </el-col>
      </el-row>
      <el-row class="hidden-md-and-up">
        <el-col :span="8">
          <h3>付费区</h3>
        </el-col>
        <el-col :span="4" :offset="11">
          <router-link to="/costlistpage">
            <el-button class="phone-more-list" type="text">更多
              <i class="el-icon-more el-icon--right"></i>
            </el-button>
          </router-link>
        </el-col>
      </el-row>
      <el-row>
      <br>
      </el-row>
      <el-row
        :gutter="30"
        class="hidden-sm-and-down"
        type="flex"
        justify="center"
        id="cost1">
        <el-col
          :span="6"
          v-for="item in costList1"
          :key="item.id"
          :offset="item.id > 6 ? 2 : 0">
          <el-card :body-style="{ padding: '0px' }" class="card-one">
            <img :src="item.profileUrl" class="recomimg">
            <div class="only-div">
              <span>{{ item.name }}</span>
              <div class="bottom clearfix">
                <router-link
                  id="logo"
                  :to="{name:'intro',params:{courseid: item.id, user: user}}">
                  <el-button type="text" class="button">点击观看</el-button>
                </router-link>
              </div>
            </div>
          </el-card>
        </el-col>
      </el-row>

      <div class="hidden-md-and-up">
        <div class="video-list">
          <ul class="vd-list">
            <li v-for="item in costList1" :key="item.id" class="list-one">
              <el-container class="list-one-outer">
                <el-aside class="aside">
                  <router-link
                    id="logo"
                    :to="{name:'intro',params:{courseid: item.id, user: user}}">
                    <img
                      :src="item.profileUrl"
                      :alt="item.name"
                      class="img-list">
                  </router-link>
                </el-aside>
                <el-container class="list-one-inner">
                  <el-header class="header">
                    <div>{{ item.name }}</div>
                  </el-header>
                  <el-main class="main">
                    <router-link
                      id="logo"
                      :to="{name:'intro',params:{courseid: item.id, user: user}}">
                      <el-button
                        icon="el-icon-caret-right"
                        type="primary"
                        class="read">点击观看
                      </el-button>
                    </router-link>
                  </el-main>
                </el-container>
              </el-container>
              <hr />
            </li>
          </ul>
        </div>
      </div>

      <el-row
        :gutter="30"
        class="hidden-sm-and-down"
        type="flex"
        justify="center"
        id="cost2">
        <el-col
          :span="6"
          v-for="item in costList2"
          :key="item.id"
          :offset="item.id > 9 ? 2 : 0">
          <el-card :body-style="{ padding: '0px' }" class="card-one">
            <img :src="item.profileUrl" class="recomimg">
            <div class="only-div">
              <span>{{ item.name }}</span>
              <div class="bottom clearfix">
                <router-link
                  id="logo"
                  :to="{name:'intro',params:{courseid: item.id, user: user}}">
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
    <div class="hidden-sm-and-down" id="footer">
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
      user: '0',
      imgList: [
        {
          id: 0,
          profileUrl: require('../../assets/images/banner1.jpg')
        },
        {
          id: 1,
          profileUrl: require('../../assets/images/banner1.jpg')
        },
        {
          id: 2,
          profileUrl: require('../../assets/images/banner1.jpg')
        }
      ],
      freeList1: [
        {
          id: 0,
          profileUrl: require('../../assets/images/free.jpg'),
          name: '啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊'
        },
        {
          id: 1,
          profileUrl: require('../../assets/images/free.jpg'),
          name: '啊啊啊啊啊'
        },
        {
          id: 2,
          profileUrl: require('../../assets/images/free.jpg'),
          name: '啊啊啊啊啊'
        }
      ],
      freeList2: [
        {
          id: 3,
          profileUrl: require('../../assets/images/free.jpg'),
          name: '呜呜呜呜呜呜呜呜'
        },
        {
          id: 4,
          profileUrl: require('../../assets/images/free.jpg'),
          name: '呜呜呜呜呜呜呜呜'
        },
        {
          id: 5,
          profileUrl: require('../../assets/images/free.jpg'),
          name: '啊啊啊啊啊'
        }
      ],
      costList1: [
        {
          id: 6,
          profileUrl: require('../../assets/images/paid.jpg'),
          name: '喵喵喵喵喵'
        },
        {
          id: 7,
          profileUrl: require('../../assets/images/paid.jpg'),
          name: '喵喵喵喵喵'
        },
        {
          id: 8,
          profileUrl: require('../../assets/images/paid.jpg'),
          name: '喵喵喵喵喵'
        }
      ],
      costList2: [
        {
          id: 9,
          profileUrl: require('../../assets/images/paid.jpg'),
          name: '喵喵喵喵喵'
        },
        {
          id: 10,
          profileUrl: require('../../assets/images/paid.jpg'),
          name: '喵喵喵喵喵'
        },
        {
          id: 11,
          profileUrl: require('../../assets/images/paid.jpg'),
          name: '喵喵喵喵喵'
        }
      ],
      login: false,
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
      }
    }
  },
  methods: {
    createRandom: function() {
      var code = Math.floor(Math.random() * (99999 - 0) + 100000)
      this.loForm.password = code.toString()
    },
    loginFunction: function() {
      if (this.loForm.delivery === false) {
        this.$message({
          message: '请输入正确的手机号和对应的验证码！',
          type: 'warning'
        })
        return
      }
      if (this.loForm.usercode !== this.loForm.password) {
        this.$message({
          message: '请输入正确的验证码！',
          type: 'warning'
        })
        return
      }
      this.loginFormVisible = false
      axios.post(utils.getURL() + 'api/authenticate/', qs.stringify({
        phone_number: this.loForm.phoneNumber,
        verification_code: 0
      })).then(response => {
        this.login = true
        this.$store.commit('setUserId', this.loForm.phoneNumber)
        this.user = this.$store.state.userId
      })
    },
    getVerification: function() {
      if (this.loForm.phoneNumber === '') {
        this.$message({
          message: '请输入正确的手机号！',
          type: 'warning'
        })
        return
      }
      this.createRandom()
      axios.post(utils.getURL() + 'api/getcode/', qs.stringify({
        phone_number: this.loForm.phoneNumber,
        password: this.loForm.password
      })).then(response => {
        this.loForm.delivery = true
      })
    },
    logout: function() {
      axios.post(utils.getURL() + 'api/logout/').then(response => {
        this.login = false
        this.$store.commit('setUserId', '0')
      })
    },
    addList: function(list, list1, list2, length) {
      let course = {
        id: '',
        profileUrl: '',
        name: ''
      }
      let tempLen = length > 3 ? 3 : length
      for (let i = 0; i < tempLen; i++) {
        course.id = list[i].pk
        course.profileUrl = utils.getURL() + 'media/' +
          list[i].fields.profile_url
        course.name = list[i].fields.course_name
        list1.push(course)
      }
      for (let i = 3; i < length; i++) {
        course.id = list[i].pk
        course.profileUrl = utils.getURL() + 'media/' +
          list[i].fields.profile_url
        course.name = list[i].fields.course_name
        list2.push(course)
      }
    }
  },
  created: function () {
    this.user = this.$store.state.userId
    if (this.user !== '0') {
      this.login = true
    }
    axios.post(utils.getURL() + 'api/listrecommend/').then(response => {
      let length = response.data.courses.length
      for (let i = 0; i < length; i++) {
        this.imgList[i].id = response.data.courses[i].id
        this.imgList[i].profileUrl = utils.getURL() + 'media/' +
          response.data.courses[i].profile_url
      }
    })
    axios.post(utils.getURL() + 'api/listfreeindex/').then(response => {
      let list = response.data.courses
      let length = list.length
      this.freeList1 = []
      this.freeList2 = []
      this.addList(list, this.freeList1, this.freeList2, length)
    })
    axios.post(utils.getURL() + 'api/listpricedindex/').then(response => {
      let list = response.data.courses
      let length = list.length
      this.costList1 = []
      this.costList2 = []
      this.addList(list, this.costList1, this.costList2, length)
    })
  }
}
</script>

<style scoped>
  .only-div {
    padding: 14px;
  }
  .index {
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
  .user-ope {
    color: white;
    font-size: 18px;
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
    max-width: 1200px;
    margin: 20px auto 20px auto;
  }
  .cost-list {
    max-width: 1200px;
    margin: 20px auto 20px auto;
  }
  .get-check {
    margin-left: 100px !important;
  }
  .more-list {
    width: 100%;
    height: 100%;
    border-radius: 5px;
    font-size: 25px;
    color: grey;
  }
  .phone-more-list {
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
  @media screen and (max-width: 800px) {
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
      color: white;
      font-size: 15px;
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
    .video-list {
      zoom: 1;
      height: 400px;
      margin-bottom: 20px;
    }
    .list-one-outer {
      max-width: 350px;
    }
    .list-one-inner {
      max-width: 200px;
    }
    .list-one {
      display: block;
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
  @media screen and (min-width: 800px) and (max-width: 1200px){
    .video-list {
      zoom: 1;
      height:300px;
      margin-bottom: 30px;
    }
    .list-one-outer {
      max-width: 500px;
    }
    .list-one-inner {
      max-width: 300px;
    }
    .list-one {
      display: block;
      float: left;
      max-width: 500px;
      margin: 5px 0px;
    }
    .aside {
      max-width: 200px !important;
    }
    .img-list {
      max-width: 200px;
      height: 150px;
    }
    .header {
      max-width: 300px;
      height: 100px !important;
    }
    .main {
      max-width: 300px;
      height: 50px;
      padding: 10px;
      text-align: right;
    }
    .read {
      padding: 5px;
    }
  }
</style>
