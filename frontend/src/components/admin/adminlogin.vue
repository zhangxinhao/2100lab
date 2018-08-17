<template>
<div class="background" style="">
  <div class="loginform">
    <el-form :model="loform" :rules="rules" style="margin-top: 12%;">
      <h1>欢迎你，科学队长管理者</h1>
      <el-form-item label="用户名" :label-width="loginLabelWidth" prop="adminId">
        <el-col :span="18">
          <el-input v-model="loform.adminId" auto-complete="true" clearable required="required" oninvalid="this.setCustomValidity('warning')"></el-input>
        </el-col>
      </el-form-item>
      <el-form-item label="密  码" :label-width="loginLabelWidth" prop="password">
        <el-col :span="18">
          <el-input v-model="loform.password" type="password" auto-complete="off" clearable required="required" oninvalid="this.setCustomValidity('warning')"></el-input>
        </el-col>
      </el-form-item>
    </el-form>
    <div slot="footer" class="login-footer">
      <router-link to="/baseadmin">
        <el-button type="primary" @click="loginFormVisible = false">登录</el-button>
      </router-link>
    </div>
  </div>
</div>
</template>
<script>
export default {
  data() {
    var validateAdminId = (rule, value, callback) => {
      if (!this.loform.adminId) {
        return callback(new Error('用户名不能为空'))
      }
    }
    var validatePassword = (rule, value, callback) => {
      if (!this.loform.password) {
        return callback(new Error('密码不能为空'))
      }
    }
    return {
      loginFormVisible: true,
      loginLabelWidth: '100px',
      loform: {
        adminId: '',
        password: ''
      },
      rules: {
        adminId: [{ required: true, validator: validateAdminId, trigger: 'blur' }],
        password: [{ required: true, validator: validatePassword, trigger: 'blur' }]
      }
    }
  },
  methods: {
  }
}
</script>

<style scoped>
  .loginform {
    width: 400px;
    height: 300px;
    border: 2px solid skyblue;
    border-radius: 10px;
    text-align: center;
    margin-left: 33%;
    background-color: rgb(236, 242, 243);
  }

  h1 {
    font-size: 100%;
    margin-bottom: 8%;
  }

  .background {
    width: 100%;
    height: 100px;
    background: linear-gradient(lightskyblue, white);
    padding-top: 120px;
  }
</style>
