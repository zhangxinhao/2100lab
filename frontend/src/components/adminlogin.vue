<template>
<div class="logindialog">
  <el-dialog title="管理员登录" :visible.sync="loginFormVisible" width="400px" height="700px">
    <el-form :model="loform" :rules="rules">
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
      <el-button @click="loginFormVisible = false">取 消</el-button>
      <el-button type="primary" @click="loginFormVisible = false">确 定</el-button>
    </div>
  </el-dialog>
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
        password: '',
        delivery: false,
        type: [],
        resource: '',
        desc: ''
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
<style>
</style>