<template>
  <div class="free-list">
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
              @click="loginFormVisible = true">登录
            </el-button>
          </td>
          <td>
            <router-link to="/personal">
              <el-button
                class="user-ope"
                type="text"
                v-if="login">个人中心
              </el-button>
            </router-link>
          </td>
          <td>
            <el-button
              class="user-ope"
              type="text"
              v-if="login"
              @click="logout">登出
            </el-button>
          </td>
        </tr>
      </table>
    </div>

    <div class="login-dialog">
      <el-dialog
        title="登录"
        :visible.sync="loginFormVisible"
        width="330px"
        height="500px">
        <el-form :model="loform" :rules="rules">
          <el-form-item
            label="手机号"
            :label-width="loginLabelWidth"
            prop="lophone">
            <el-col :span="18">
              <el-input
                v-model="loform.phonenumber"
                auto-complete="true"
                clearable required="required"
                pattern="/^1[3|4|5|7|8][0-9]\d{8}$/"
                oninvalid="this.setCustomValidity('warning')">
              </el-input>
            </el-col>
          </el-form-item>
          <el-form-item label="验证码" :label-width="loginLabelWidth">
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
            @click="loginFormVisible = false">获取验证码
          </el-button>
          <el-button @click="loginFormVisible = false">取 消</el-button>
          <el-button
            type="primary"
            @click="loginFormVisible = false">确 定
          </el-button>
        </div>
      </el-dialog>
    </div>

    <div class="dump-button">
      <el-button type="primary" disabled>免费区</el-button>
      <router-link to="/costlistpage">
        <el-button>付费区</el-button>
      </router-link>
    </div>

    <div class="main-inner">
      <div class="container-body">
        <div class="video-list">
          <ul class="vd-list">
            <li v-for="item in freeList" :key="item.id" class="list-one">
              <el-container class="list-one-outer">
                <el-aside class="aside">
                  <router-link
                    id="logo"
                    :to="{name:'intro',
                      params:{courseid: item.id, user: user}}">
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
                      :to="{name:'intro',
                        params:{courseid: item.id, user: user}}">
                      <el-button
                        icon="el-icon-caret-right"
                        type="primary"
                        class="read">点击阅读
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
      <el-footer>
      <div class="pager">
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
      </el-footer>
    </div>
    <div class="hidden-md-and-down" id="footer">
      <img src="../../assets/footer1.png" width=100%>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
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
      login: true,
      not_login: false,
      loginFormVisible: false,
      loginLabelWidth: '100px',
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
      courses: [],
      freeList: [
        {
          id: 10,
          profileUrl: require('../../assets/images/free.jpg'),
          name: '啊啊啊啊啊'
        },
        {
          id: 11,
          profileUrl: require('../../assets/images/free.jpg'),
          name: '啊啊啊啊啊'
        },
        {
          id: 12,
          profileUrl: require('../../assets/images/free.jpg'),
          name: '啊啊啊啊啊'
        },
        {
          id: 13,
          profileUrl: require('../../assets/images/free.jpg'),
          name: '啊啊啊啊啊'
        },
        {
          id: 14,
          profileUrl: require('../../assets/images/free.jpg'),
          name: '啊啊啊啊啊'
        },
        {
          id: 15,
          profileUrl: require('../../assets/images/free.jpg'),
          name: '啊啊啊啊啊'
        },
        {
          id: 16,
          profileUrl: require('../../assets/images/free.jpg'),
          name: '啊啊啊啊啊'
        },
        {
          id: 17,
          profileUrl: require('../../assets/images/free.jpg'),
          name: '啊啊啊啊啊'
        },
        {
          id: 18,
          profileUrl: require('../../assets/images/free.jpg'),
          name: '啊啊啊啊啊'
        },
        {
          id: 19,
          profileUrl: require('../../assets/images/free.jpg'),
          name: '啊啊啊啊啊'
        },
        {
          id: 20,
          profileUrl: require('../../assets/images/free.jpg'),
          name: '啊啊啊啊啊'
        },
        {
          id: 21,
          profileUrl: require('../../assets/images/free.jpg'),
          name: '啊啊啊啊啊'
        }
      ],
      pageSize: 12,
      totalNumber: 100,
      pageNo: 1
    }
  },
  methods: {
    flipeOver: function (page) {
      let totalEnd = this.pageSize * page
      let end = this.totalNumber < (totalEnd) ? this.totalNumber : totalEnd
      this.freeList = []
      let start = this.pageSize * (page - 1)
      for (let i = start; i < end; i++) {
        this.freeList.push(this.courses[i])
      }
    }
  },
  created: function () {
    axios.post(utils.getURL() + 'api/listfreecourses/').then(response => {
      let list = response.data.courses
      let length = list.length
      let course = {
        id: '',
        profileUrl: '',
        name: ''
      }
      for (let i = 0; i < length; i++) {
        course.id = list[i].pk
        course.profileUrl = utils.getURL() + 'media/' +
          list[i].fields.profile_url
        course.name = list[i].fields.course_name
        this.courses.push(course)
      }
      this.totalNumber = this.courses.length
      let totalNumber = this.totalNumber
      this.freeList = []
      let size = this.pageSize
      if (totalNumber < size) {
        this.freeList = this.courses
      } else {
        for (let i = 0; i < size; i++) {
          this.freeList.push(this.courses[i])
        }
      }
    })
  }
}
</script>

<style scoped>
  .el-pagination {
    text-align: center;
  }
  .free-list {
    background-color: rgb(240, 240, 240);
  }
  .dump-button {
    margin-top: 50px;
    margin-left: 50px;
    margin-bottom: 50px;
  }
  .tool-bar {
    width: 100%;
    min-height: 45px;
    max-height: 70px;
    padding: 0;
    background-color:#409EFF;
  }
  #footer {
    color: #333;
    text-align: center;
    line-height: 55px;
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
  body {
    margin: 0;
  }

  #app {
    margin: 0;
    padding: 0;
  }

  .free-list {
    margin: 0;
    padding: 0;
  }

  li, ul {
    list-style: none;
    margin: 10px 10px;
  }
  .menu {
    position: relative;
    height: 50px;
    margin: 0, auto;
    padding: 8px 0 0;
    margin-top: 10px;
    margin-bottom: 30px;
    z-index: 99;
  }
  .main-inner {
    max-width: 1250px;
    height: 1250px;
    margin: 0 auto;
    position: relative;
    zoom: 1;
  }
  .video-list {
    zoom: 1;
    height: 1150px;
    margin-bottom: 30px;
  }
  .list-one-outer {
    width: 550px;
  }
  .list-one-inner {
    width: 350px;
  }
  .list-one {
    display: block;
    float: left;
    width: 550px;
    margin: 10px 10px;
  }
  .aside {
    width: 200px !important;
  }
  .img-list {
    width: 200px;
    height: 150px;
  }
  .header {
    width: 320px;
    height: 90px !important;
  }
  .main {
    width: 320px;
    height: 50px;
    padding: 10px;
    text-align: right;
  }
  .pager {
    text-align: right;
  }
  @media screen and (max-width: 800px) {
    li, ul {
      list-style: none;
      margin: 5px 10px;
      padding: 0px;
    }
    .user-ope {
      color: white;
      font-size: 15px;
    }
    .main-inner {
      max-width: 1250px;
      height: 1580px;
      margin: 0 auto;
      position: relative;
      zoom: 1;
    }
    .video-list {
      zoom: 1;
      height: 1580px;
      margin-bottom: 30px;
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
  }
  @media screen and (min-width: 800px) and (max-width: 1100px){
    li, ul {
      list-style: none;
      margin: 5px 10px;
      padding: 0px;
    }
    .user-ope {
      color: white;
      font-size: 15px;
    }
    .main-inner {
      max-width: 1250px;
      height: 1080px;
      margin: 0 auto;
      position: relative;
      zoom: 1;
    }
    .video-list {
      zoom: 1;
      height: 1080px;
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
  @media screen and (min-width: 500px) and (max-width: 800px) {
    .main-inner {
      max-width: 1250px;
      height: 780px;
      margin: 0 auto;
      position: relative;
      zoom: 1;
    }
    .video-list {
      zoom: 1;
      height: 780px;
      margin-bottom: 30px;
    }
  }
</style>
