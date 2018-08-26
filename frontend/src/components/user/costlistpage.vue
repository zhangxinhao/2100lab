<template>
<div class="costlist">

  <div class="toolbar">
    <div class="logo">
      <img src="../../assets/logo1.png" width="200%" height="100%">
    </div>
    <table align="right">
      <tr>
        <td>
          <el-button class="user-ope"
            type="text"
            v-if="!login"
            @click="loginFormVisible = true">登录/注册
          </el-button>
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
    <el-dialog title="登录" :visible.sync="loginFormVisible" width="330px" height="500px">
      <el-form :model="loform" :rules="rules">
        <el-form-item label="手机号" :label-width="loginLabelWidth" prop="lophone">
          <el-col :span="18">
            <el-input v-model="loform.phonenumber"
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

 <div class="dumpbutton">
    <router-link to="/freelistpage">
      <el-button  type="primary">免费区</el-button>
    </router-link>
    <el-button type="primary" disabled>付费区</el-button>
  </div>

  <div class="main-inner">
    <div class="container-body">
      <div class="video-list">
        <ul class="vd-list">
          <li v-for="item in costList" :key="item.id" class="listone">
            <el-container class="listone-outer">
              <el-aside class="aside">
                <router-link id="logo" :to="{name:'intro',params:{courseid: item.id}}">
                  <img :src="item.profile_url" :alt="item.name" class="imgList">
                </router-link>
              </el-aside>
              <el-container class="listone-inner">
                <el-header class="header"><div>{{item.name}}</div></el-header>
                <el-main class="main">
                  <el-button icon="el-icon-caret-right" type="primary" class="read">点击阅读</el-button>
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
          :total="totalnumber"
          :current-page.sync="pageNo"
          :pager-count="7"
          @current-change="flipeOver"
        >
      </el-pagination>
    </div>
    </el-footer>
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
        lophone: [{ required: true, validator: validateloPhone, trigger: 'blur' }]
      },
      courses: [],
      costList: [
        {id: 10, profile_url: require('../../assets/images/paid.jpg'), name: '啊啊啊啊啊'},
        {id: 11, profile_url: require('../../assets/images/paid.jpg'), name: '啊啊啊啊啊'},
        {id: 12, profile_url: require('../../assets/images/paid.jpg'), name: '啊啊啊啊啊'},
        {id: 13, profile_url: require('../../assets/images/paid.jpg'), name: '啊啊啊啊啊'},
        {id: 14, profile_url: require('../../assets/images/paid.jpg'), name: '啊啊啊啊啊'},
        {id: 15, profile_url: require('../../assets/images/paid.jpg'), name: '啊啊啊啊啊'},
        {id: 16, profile_url: require('../../assets/images/paid.jpg'), name: '啊啊啊啊啊'},
        {id: 17, profile_url: require('../../assets/images/paid.jpg'), name: '啊啊啊啊啊'},
        {id: 18, profile_url: require('../../assets/images/paid.jpg'), name: '啊啊啊啊啊'},
        {id: 19, profile_url: require('../../assets/images/paid.jpg'), name: '啊啊啊啊啊'},
        {id: 20, profile_url: require('../../assets/images/paid.jpg'), name: '啊啊啊啊啊'},
        {id: 21, profile_url: require('../../assets/images/paid.jpg'), name: '啊啊啊啊啊'}
      ],
      pageSize: 12,
      totalnumber: 100,
      pageNo: 1
    }
  },
  methods: {
    flipeOver: function (page) {
      let _end = this.pageSize * page
      let end = this.totalnumber < (_end) ? this.totalnumber : _end
      this.costList = []
      let start = this.pageSize * (page - 1)
      for (let i = start; i < end; i++) {
        this.costList.push(this.courses[i])
      }
    }
  },
  created: function () {
    axios.post(utils.getURL() + 'api/listpricedcourses/').then(response => {
      this.courses = response.data.courses
      this.totalnumber = this.courses.length
      let totalnumber = this.totalnumber
      this.costList = []
      let size = this.pageSize
      if (totalnumber < size) {
        this.costList = this.courses
      } else {
        for (let i = 0; i < size; i++) {
          this.costList.push(this.courses[i])
        }
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
  .dumpbutton {
    margin-top: 50px;
    margin-left: 50px;
    margin-bottom: 50px;
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
  body {
    margin: 0;
  }

  #app {
    margin: 0;
    padding: 0;
  }

  .costlist {
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
    height:1150px;
    margin-bottom: 30px;
  }
  .listone-outer {
    width: 550px;
  }
  .listone-inner {
    width: 350px;
  }
  .listone {
    display: block;
    float: left;
    width: 550px;
    margin: 10px 10px;
  }
  .aside {
    width: 200px !important;
  }
  .imgList {
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
      color:#085078;
      font-size:15px;
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
      height:1580px;
      margin-bottom: 30px;
    }
    .listone-outer {
      max-width: 350px;
    }
    .listone-inner {
      max-width: 200px;
    }
    .listone {
      display: block;
      float: left;
      max-width: 350px;
      margin: 5px 0px;
    }
    .aside {
      max-width: 150px !important;
    }
    .imgList {
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
  @media screen and (min-width: 800px) and (max-width: 1100px){
    li, ul {
      list-style: none;
      margin: 5px 10px;
      padding: 0px;
    }
    .user-ope {
      color:#085078;
      font-size:15px;
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
      height:1080px;
      margin-bottom: 30px;
    }
    .listone-outer {
      max-width: 500px;
    }
    .listone-inner {
      max-width: 300px;
    }
    .listone {
      display: block;
      float: left;
      max-width: 500px;
      margin: 5px 0px;
    }
    .aside {
      max-width: 200px !important;
    }
    .imgList {
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
      height:780px;
      margin-bottom: 30px;
    }
  }
</style>
