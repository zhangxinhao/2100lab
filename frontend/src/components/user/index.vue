<!-- Add "scoped" attribute to limit CSS to this component only -->
<template>
  <div class="index">
    <div class="toolbar">
      <table align="right">
        <tr>
          <td>
            <el-button class="user-ope" type="text" v-if="!login" @click="loginFormVisible = true" style="color:#085078;font-size:18px">登录&nbsp;&nbsp;&nbsp;</el-button>
          </td>
          <td>
            <el-button class="user-ope" type="text" v-if="!login" @click="registerFormVisible = true" style="color:#085078;font-size:18px">注册</el-button>
          </td>
          <td>
            <el-button class="user-ope" type="text" v-if="login" @click="logout" style="color:white">登出</el-button>
          </td>
          <td>&nbsp;&nbsp;&nbsp;&nbsp;</td>
        </tr>
      </table>
    </div>

    <div class="carousel">
      <el-carousel :interval="4000" type="card" height="350px">
        <el-carousel-item v-for="item in imgList" :key="item.id">
          <el-row>
            <router-link id="logo" :to="{name:'intro',params:{courseid: item.id}}">
              <el-col :span="24"><img ref="500px" height="100%" width="100%" :src="item.profile_url" class="banner_img"/></el-col>
            </router-link>
          </el-row>
        </el-carousel-item>
      </el-carousel>
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

    <div>&nbsp;</div>
    <hr />
    <div>&nbsp;</div>
    <div class="free-list">
      <el-row :gutter="30">
        <el-col :span="8">
          <h1 style="text-align:left;">免费区</h1>
        </el-col>
      </el-row>
      <el-row>
        <div>&nbsp;</div>
      </el-row>
      <el-row :gutter="30">
        <el-col v-for="item in freeList_1" :key="item.id" :span="8">
          <router-link id="logo" :to="{name:'intro',params:{courseid: item.id}}">
            <img :src="item.profile_url" width="350px" height="250px" >
            <div style="display:inline word-break:break-all word-wrap:break-word">{{item.name}}</div>
          </router-link>
        </el-col>
      </el-row>
      <el-row :gutter="30">
        <el-col v-for="item in freeList_2" :key="item.id" :span="8">
          <router-link id="logo" :to="{name:'intro',params:{courseid: item.id}}">
            <img :src="item.profile_url" width="350px" height="250px">
            <div style="display:inline word-break:break-all word-wrap:break-word">{{item.name}}</div>
          </router-link>
        </el-col>
        <el-col :span="8">
          <router-link to="/freelistpage">
            <el-button icon="el-icon-more" class="morelist">更多</el-button>
          </router-link>
        </el-col>
      </el-row>
    </div>

    <div>&nbsp;</div>
    <hr />
    <div>&nbsp;</div>

    <div class="cost-list">
      <el-row :gutter="20">
        <el-col :span="8">
          <h1 style="text-align:left;">付费区</h1>
        </el-col>
      </el-row>
      <el-row>
        <div>&nbsp;</div>
      </el-row>
      <el-row :gutter="20">
        <el-col v-for="item in costList_1" :key="item.id" :span="8">
          <router-link id="logo" :to="{name:'intro',params:{courseid: item.id}}">
            <img :src="item.profile_url" width="350px" height="250px" >
            <div style="display:inline word-break:break-all word-wrap:break-word">{{item.name}}</div>
          </router-link>
        </el-col>
      </el-row>
      <el-row :gutter="20">
        <el-col v-for="item in costList_2" :key="item.id" :span="8">
          <router-link id="logo" :to="{name:'intro',params:{courseid: item.id}}">
            <img :src="item.profile_url" width="350px" height="250px">
            <div style="display:inline word-break:break-all word-wrap:break-word">{{item.name}}</div>
          </router-link>
        </el-col>
        <el-col :span="8">
          <router-link to="/costlistpage">
            <el-button icon="el-icon-more" class="morelist">更多</el-button>
          </router-link>
        </el-col>
      </el-row>
    </div>
    <br />
    <br />
    <br />
    <el-footer height="50px">2100实验室 联系电话：010-86398756 关注我们：微信服务号：科学队长</el-footer>

  </div>
</template>

<script>
import axios from 'axios'
import qs from 'qs'

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
      imgList: [
        {id: 0, profile_url: require('../../assets/images/banner1.jpg')},
        {id: 1, profile_url: require('../../assets/images/banner1.jpg')},
        {id: 2, profile_url: require('../../assets/images/banner1.jpg')}
      ],
      freeList_1: [
        {id: 0, profile_url: require('../../assets/images/free.jpg'), name: '啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊'},
        {id: 1, profile_url: require('../../assets/images/free.jpg'), name: '啊啊啊啊啊'},
        {id: 2, profile_url: require('../../assets/images/free.jpg'), name: '啊啊啊啊啊'}
      ],
      freeList_2: [
        {id: 3, profile_url: require('../../assets/images/free.jpg'), name: '呜呜呜呜呜呜呜呜'},
        {id: 4, profile_url: require('../../assets/images/free.jpg'), name: '呜呜呜呜呜呜呜呜'}
      ],
      costList_1: [
        {id: 5, profile_url: require('../../assets/images/paid.jpg'), name: '喵喵喵喵喵'},
        {id: 6, profile_url: require('../../assets/images/paid.jpg'), name: '喵喵喵喵喵'},
        {id: 7, profile_url: require('../../assets/images/paid.jpg'), name: '喵喵喵喵喵'}
      ],
      costList_2: [
        {id: 8, profile_url: require('../../assets/images/paid.jpg'), name: '喵喵喵喵喵'},
        {id: 9, profile_url: require('../../assets/images/paid.jpg'), name: '喵喵喵喵喵'}
      ],
      login: true,
      not_login: false,
      loginFormVisible: false,
      loginLabelWidth: '100px',
      loform: {
        phonenumber: '',
        password: '',
        delivery: false,
        usercode: ''
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
      axios.post('http://192.168.55.33:8000/api/authenticate/', qs.stringify({
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
      axios.post('http://192.168.55.33:8000/api/getcode/', qs.stringify({
        phone_number: this.loform.phonenumber,
        password: this.loform.password
      })).then(
        response => {
          this.loform.delivery = true
        }
      )
    },
    logout: function() {
      axios.post('http://192.168.55.33:8000/api/logout/').then(response => {
        this.login = false
      })
    }
  },
  created: function () {
    axios.post('http://192.168.55.33:8000/api/login/').then(response => {
      this.login = response.data.status
    })
    axios.post('http://192.168.55.33:8000/api/listrecommend/').then(response => {
      this.imgList = response.data.courses
    })
    axios.post('http://192.168.55.33:8000/api/listfreeindex/').then(response => {
      this.freeList_1 = []
      this.freeList_2 = []
      let freelist = response.data.courses
      for (let i = 0; i < 3; i++) {
        this.freeList_1.push(freelist[i])
      }
      for (let i = 3; i < 5; i++) {
        this.freeList_2.push(freelist[i])
      }
    })
    axios.post('http://192.168.55.33:8000/api/listpricedindex/').then(response => {
      this.costList_1 = []
      this.costList_2 = []
      let costList = response.data.courses
      for (let i = 0; i < 3; i++) {
        this.costList_1.push(costList[i])
      }
      for (let i = 3; i < 5; i++) {
        this.costList_2.push(costList[i])
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

  #user-ope {
    margin-right: 100px;
   }

  .index {
    /* width: 1200px; */
    margin: 0 auto;
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

  .carousel {
    width: 1200px;
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
    width:1200px;
    /* height:550px; */
    margin:20px auto 20px auto;
    /* background-color: black; */
  }
  .cost-list {
    width:1200px;
    /* height:550px; */
    margin:20px auto 20px auto;
    /* background-color: black; */
  }
  .morelist {
    width: 350px;
    height: 250px;
    /* background:rgb(149, 202, 255); */
    border: 2px, solid, black;
    border-radius: 5px;
    font-size: 30px;
    /* opacity: 0.7; */
    color: grey;
  }
  .morelist:hover {
    background-color:rgb(240, 240, 240);
    opacity: 0.7;
    color:black;
  }
  hr {
    width: 1200px;
  }
</style>
