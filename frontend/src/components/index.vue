<!-- Add "scoped" attribute to limit CSS to this component only -->
<template>

  <div class="index">
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

    <div class="carousel">
      <el-carousel :interval="4000" type="card" height="500px">
        <el-carousel-item v-for="item in imgList" :key="item.id">
          <el-row>
            <el-col :span="24"><img ref="500px" :src="item.idView" class="banner_img"/></el-col>
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

  </div>
</template>

<script>
export default {
  data() {
    var phoneReg = /^1[3|4|5|7|8][0-9]\d{8}$/
    var validateloPhone = (rule, value, callback) => {
      console.log(this.loform.phonenumber)
      if (!this.loform.phonenumber) {
        return callback(new Error('号码不能为空'))
      }
      setTimeout(() => {
        if (!phoneReg.test(this.loform.phonenumber)) {
          console.log('geshi')
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
        {id: 0, idView: require('../assets/images/banner1.jpg')},
        {id: 1, idView: require('../assets/images/banner1.jpg')},
        {id: 2, idView: require('../assets/images/banner1.jpg')}
      ],
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
      }
    }
  },
  methods: {

  }
}
</script>

<style>
  body {
    margin: 0;
  }

  #app {
    margin: 0;
    padding: 0;
  }

  #user-ope {
    margin-right: 100px;
   }

  .index {
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

  .carousel {
    width: 1500px;
    text-align: center;
    margin: 20px auto;
  }
  .banner_img {
    height: 100%;
  }

</style>
