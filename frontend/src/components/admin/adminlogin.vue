<template>
<div class="background">
  <div class="login-form">
    <el-form :model="loForm" :rules="rules" class="form-thing">
      <h1>欢迎你，科学队长管理者</h1>
      <el-form-item label="用户名"
        :label-width="loginLabelWidth"
        prop="adminId">
        <el-col :span="18">
          <el-input
            v-model="loForm.adminId"
            auto-complete="true"
            clearable
            required="required"
            oninvalid="this.setCustomValidity('warning')">
          </el-input>
        </el-col>
      </el-form-item>
      <el-form-item label="密  码"
        :label-width="loginLabelWidth"
        prop="password">
        <el-col :span="18">
          <el-input
            v-model="loForm.password"
            type="password"
            auto-complete="off"
            clearable
            required="required"
            oninvalid="this.setCustomValidity('warning')">
          </el-input>
        </el-col>
      </el-form-item>
    </el-form>
    <div slot="footer" class="login-footer">
      <el-button type="primary" @click="login">登录</el-button>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'
import qs from 'qs'
import * as utils from '../utils/utils.js'
import * as hash from '../utils/hash.js'

export default {
  data() {
    let validateAdminId = (rule, value, callback) => {
      if (!this.loForm.adminId) {
        return callback(new Error('用户名不能为空'))
      }
    }
    let validatePassword = (rule, value, callback) => {
      if (!this.loForm.password) {
        return callback(new Error('密码不能为空'))
      }
    }
    return {
      loginLabelWidth: '100px',
      loForm: {
        adminId: '',
        password: ''
      },
      rules: {
        adminId: [
          {
            required: true,
            validator: validateAdminId,
            trigger: 'blur'
          }
        ],
        password: [
          {
            required: true,
            validator: validatePassword,
            trigger: 'blur'
          }
        ]
      }
    }
  },
  methods: {
    login: function() {
      axios.post(utils.getURL() + 'api/adminlogin/', qs.stringify({
        username: this.loForm.adminId,
        password: hash.getHash(this.loForm.password)
      })).then(response => {
        let status = response.data.status
        if (status === 0) {
          this.$store.commit('setUserId', this.loForm.adminId)
          this.$router.push({ path: '/baseAdmin' })
        } else {
          return this.$message.error('登录失败')
        }
      })
    }
  }
}
</script>

<style scoped>
  .login-form {
    width: 400px;
    height: 300px;
    border: 2px solid rgb(209, 214, 216);
    background: transparent;
    text-align: center;
    margin: auto;
    background-color: #EBEEF5;
    filter:alpha(Opacity=60);-moz-opacity:0.7;opacity: 0.8;
    position: relative;
    top: 50%;
    transform: translate(0,50%);
  }
  h1 {
    font-size: 100%;
    margin-bottom: 8%;
  }
  .background {
    width: 100%;
    background-image: url(../../assets/back1.jpg);
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
    min-height: 100vh;
  }
  .form-thing {
    margin-top: 12%;
  }
</style>
