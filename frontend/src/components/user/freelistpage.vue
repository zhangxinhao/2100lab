<template>
<div class="freelist">

  <div class="toolbar">
    <table align="right">
      <tr>
        <td>
          <el-button class="user-ope" type="text" v-if="login" @click="loginFormVisible = true">登录/注册&nbsp;&nbsp;</el-button>
        </td>
        <td>
          <el-button class="user-ope" type="text" v-if="not_login" @click="logout" style="color:white">登出</el-button>
        </td>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;</td>
      </tr>
    </table>
  </div>

  <div class="logindialog">
    <el-dialog title="登录" :visible.sync="loginFormVisible" width="330px" height="500px">
      <el-form :model="loform" :rules="rules">
        <el-form-item label="手机号" :label-width="loginLabelWidth" prop="lophone">
          <el-col :span="18">
            <el-input v-model="loform.phonenumber" auto-complete="true" clearable required="required" pattern="/^1[3|4|5|7|8][0-9]\d{8}$/" oninvalid="this.setCustomValidity('warning')"></el-input>
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

  <div class="menu">
    <el-row :gutter="100">
      <el-col :span="1" :offset="2">
        <router-link to="/">
          <el-button icon="el-icon-back" class="backtoindex">首页</el-button>
        </router-link>
      </el-col>
      <el-col :span="1">
        <el-button type="primary" disabled>免费区</el-button>
      </el-col>
      <el-col :span="1">
        <router-link to="/costlistpage">
          <el-button>付费区</el-button>
        </router-link>
      </el-col>
    </el-row>
  </div>

  <div class="main-inner">
    <div class="container-body">
      <div class="video-list">
        <ul class="vd-list">
          <li v-for="item in freeList" :key="item.id" class="listone">
            <el-container class="listone-outer">
              <el-aside class="aside">
                <router-link id="logo" :to="{name:'intro',params:{courseid: item.id}}">
                  <img :src="item.profile_url" :alt="item.name" class="imgList">
                </router-link>
              </el-aside>
              <el-container class="listone-inner">
                <el-header class="header"><div>{{item.name}}</div></el-header>
                <el-main class="main"><el-button icon="el-icon-caret-right" type="primary" class="read">点击阅读</el-button></el-main>
              </el-container>
            </el-container>
            <hr />
          </li>
        </ul>
      </div>
    </div>
    <el-footer>
    <div style="text-align:right">
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
      freeList: [
        {id: 10, profile_url: require('../../assets/images/free.jpg'), name: '啊啊啊啊啊'},
        {id: 11, profile_url: require('../../assets/images/free.jpg'), name: '啊啊啊啊啊'},
        {id: 12, profile_url: require('../../assets/images/free.jpg'), name: '啊啊啊啊啊'},
        {id: 13, profile_url: require('../../assets/images/free.jpg'), name: '啊啊啊啊啊'},
        {id: 14, profile_url: require('../../assets/images/free.jpg'), name: '啊啊啊啊啊'},
        {id: 15, profile_url: require('../../assets/images/free.jpg'), name: '啊啊啊啊啊'},
        {id: 16, profile_url: require('../../assets/images/free.jpg'), name: '啊啊啊啊啊'},
        {id: 17, profile_url: require('../../assets/images/free.jpg'), name: '啊啊啊啊啊'},
        {id: 18, profile_url: require('../../assets/images/free.jpg'), name: '啊啊啊啊啊'},
        {id: 19, profile_url: require('../../assets/images/free.jpg'), name: '啊啊啊啊啊'},
        {id: 20, profile_url: require('../../assets/images/free.jpg'), name: '啊啊啊啊啊'},
        {id: 21, profile_url: require('../../assets/images/free.jpg'), name: '啊啊啊啊啊'}
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
      this.freeList = []
      let start = this.pageSize * (page - 1)
      for (let i = start; i < end; i++) {
        this.freeList.push(this.courses[i])
      }
    }
  },
  created: function () {
    axios.post(utils.getURL() + 'api/listfreecourses/').then(response => {
      this.courses = response.data.courses
      this.totalnumber = this.courses.length
      let totalnumber = this.totalnumber
      this.freeList = []
      let size = this.pageSize
      if (totalnumber < size) {
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
  body {
    margin: 0;
  }

  #app {
    margin: 0;
    padding: 0;
  }

  .freelist {
    margin: 0;
    padding: 0;
  }

  .toolbar {
    width: 100%;
    height: 55px;
    margin: 0;
    padding: 0;
    text-align: right;
    background-color:lightskyblue;
    background: linear-gradient(lightskyblue, white);
    opacity: 0.7;
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
  }
  .user-ope {
    color:#085078;
    font-size:18px;
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
    border-bottom: 1px, solid, black;
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
    border: 1px, solid, gray;
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
      border: 1px, solid, gray;
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
      border: 1px, solid, gray;
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
