<template>
<div class="freelist">

  <div class="toolbar">
    <table align="right">
      <tr>
        <td>
          <el-button class="user-ope" type="text" v-if="login" @click="loginFormVisible = true" style="color:#085078;font-size:18px">登录&nbsp;&nbsp;&nbsp;</el-button>
        </td>
        <td>
          <el-button class="user-ope" type="text" v-if="login" @click="registerFormVisible = true" style="color:#085078;font-size:18px">注册</el-button>
        </td>
        <td>
          <el-button class="user-ope" type="text" v-if="not_login" @click="logout" style="color:white">登出</el-button>
        </td>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;</td>
      </tr>
    </table>
  </div>

  <div class="logindialog">
    <el-dialog title="登录" :visible.sync="loginFormVisible" width="400px" height="700px">
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

  <div class="registerdialog">
    <el-dialog title="注册" :visible.sync="registerFormVisible" width="400px" height="700px">
      <el-form :model="reform" :rules="rules">
        <el-form-item label="手机号" :label-width="registerLabelWidth" prop="rephone">
          <el-col :span="18">
            <el-input v-model="reform.phonenumber" auto-complete="off" clearable required="required" pattern="/^1[3|4|5|7|8][0-9]\d{8}$/"></el-input>
          </el-col>
        </el-form-item>
        <el-form-item label="验证码" :label-width="registerLabelWidth">
          <el-col :span="18">
            <el-input v-model="reform.password" auto-complete="off" clearable></el-input>
          </el-col>
        </el-form-item>
      </el-form>
      <div slot="footer" class="register-footer">
        <el-button type="primary" @click="loginFormVisible = false">获取验证码</el-button>
        <el-button @click="registerFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="registerFormVisible = false">确 定</el-button>
      </div>
    </el-dialog>
  </div>

  <div class="menu">
    <ul>
      <li style="display:inline; width: 120px; height:20px;float:left"></li>
      <li style="display:inline">
        <router-link to="/">
          <el-button icon="el-icon-back">首页</el-button>
        </router-link>
      </li>
      <li style="display:inline">
        <el-button type="primary" disabled>免费区</el-button>
      </li>
      <li style="display:inline">
        <router-link to="/costlistpage">
         <el-button>付费区</el-button>
        </router-link>
      </li>
    </ul>
  </div>

  <div class="main-inner">
    <div class="container-body">
      <div class="video-list">
        <ul class="vd-list">
          <li v-for="item in freeList" :key="item.id" class="listone">
            <el-container class="listone-outer">
              <el-aside width="200px">
                <img :src="item.idView" :alt="item.idTitle" width="200px" height="150px">
              </el-aside>
              <el-container class="listone-inner">
                <el-header style="width:320px;height:90px"><div>{{item.idTitle}}</div></el-header>
                <el-main style="width:320px;height:50px;padding:10px;text-align:right"><el-button icon="el-icon-caret-right" type="primary">点击阅读</el-button></el-main>
              </el-container>
            </el-container>
            <hr />
          </li>
        </ul>
      </div>
    </div>

    <div style="text-align:right">
      <el-pagination
        background
        layout="prev, pager, next"
        :total="totalnumber"
        :current-page.sync="pageNo"
        :pager-count="7"
        >
      </el-pagination>
    </div>
  </div>

</div>
</template>

<script>
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
    var validaterePhone = (rule, value, callback) => {
      if (!this.reform.phonenumber) {
        return callback(new Error('号码不能为空'))
      }
      setTimeout(() => {
        if (!phoneReg.test(this.reform.phonenumber)) {
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
      registerFormVisible: false,
      registerLabelWidth: '100px',
      reform: {
        phonenumber: '',
        password: '',
        delivery: false,
        type: [],
        resource: '',
        desc: ''
      },
      rules: {
        lophone: [{ required: true, validator: validateloPhone, trigger: 'blur' }],
        rephone: [{ required: true, validator: validaterePhone, trigger: 'blur' }]
      },
      freeList: [
        {idView: require('../assets/images/free.jpg'), idTitle: '啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊'},
        {idView: require('../assets/images/free.jpg'), idTitle: '啊啊啊啊啊'},
        {idView: require('../assets/images/free.jpg'), idTitle: '啊啊啊啊啊'},
        {idView: require('../assets/images/free.jpg'), idTitle: '啊啊啊啊啊'},
        {idView: require('../assets/images/free.jpg'), idTitle: '啊啊啊啊啊'},
        {idView: require('../assets/images/free.jpg'), idTitle: '啊啊啊啊啊'},
        {idView: require('../assets/images/free.jpg'), idTitle: '啊啊啊啊啊'},
        {idView: require('../assets/images/free.jpg'), idTitle: '啊啊啊啊啊'},
        {idView: require('../assets/images/free.jpg'), idTitle: '啊啊啊啊啊'},
        {idView: require('../assets/images/free.jpg'), idTitle: '啊啊啊啊啊'},
        {idView: require('../assets/images/free.jpg'), idTitle: '啊啊啊啊啊'},
        {idView: require('../assets/images/free.jpg'), idTitle: '啊啊啊啊啊'}
      ],
      totalnumber: 100,
      pageNo: 1
    }
  },
  methods: {

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
    width: 1250px;
    height: 1250px;
    margin: 0 auto;
    position: relative;
    zoom: 1;
  }
  .video-list {
    zoom: 1;
    height:1150px;
    min-height: 400px;
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
</style>
