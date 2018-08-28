<template>
  <div class="add-admin">

    <el-form ref="newAdmin"
      :model="newAdmin"
      label-width="200px" >

      <el-form-item label="管理员编号"  >
        <el-input v-model="newAdmin.adminName" class="inp"></el-input>
      </el-form-item>

      <el-form-item label="管理员密码" >
        <el-input v-model="newAdmin.password" class="inp"></el-input>
      </el-form-item>

      <el-form-item label="课程管理权限">
        <el-switch
          v-model="newAdmin.courseManage"
          active-value="true"
          inactive-value="false"
          @change="changeC"
          class="change-c">
        </el-switch>
      </el-form-item>

      <el-form-item label="管理用户权限" >
        <el-switch
          v-model="newAdmin.userManage"
          active-value="true"
          inactive-value="false"
          @change="changeU"
          class="change-u">
        </el-switch>
      </el-form-item>

      <el-form-item label="操作历史权限">
        <el-switch
          v-model="newAdmin.operationHistory"
          active-value="true"
          inactive-value="false"
          @change="changeH"
          class="change-h">
        </el-switch>
      </el-form-item>

      <el-form-item label="订单管理权限">
        <el-switch
          v-model="newAdmin.orderManage"
          active-value="true"
          inactive-value="false"
          @change="changeO"
          class="change-o">
        </el-switch>
      </el-form-item>

      <el-form-item>
        <el-button type="primary"
          @click="onSubmit"
          class="end">
        立即创建
        </el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import axios from 'axios'
import qs from 'qs'
import * as utils from '../utils/utils.js'
import * as hash from '../utils/hash.js'

export default {
  data() {
    return {
      newAdmin: {
        adminName: '',
        password: '',
        courseManage: false,
        userManage: false,
        operationHistory: false,
        orderManage: false
      }
    }
  },
  methods: {
    changeC: function(status) {
      this.newAdmin.courseManage = status
    },
    changeU: function(status) {
      this.newAdmin.userManage = status
    },
    changeH: function(status) {
      this.newAdmin.operationHistory = status
    },
    changeO: function(status) {
      this.newAdmin.orderManage = status
    },
    onSubmit: function() {
      axios.post(utils.getURL() + 'api/createadmin/', qs.stringify({
        adminName: this.newAdmin.adminName,
        password: hash.getHash(this.newAdmin.password),
        courseManage: this.newAdmin.courseManage,
        userManage: this.newAdmin.userManage,
        operationHistory: this.newAdmin.operationHistory,
        orderManage: this.newAdmin.orderManage
      })).then(response => {
        if (response.data.status === 0) {
          this.$message({
            message: '创建成功！',
            type: 'success'
          })
          window.location.reload()
        } else {
          this.$message({
            message: '编号已存在',
            type: 'warning'
          })
        }
      })
    }
  }
}
</script>
<style scoped>
  .add-admin {
    width: 400px;
    margin-left: 200px;
    margin-top: 50px;
  }
</style>
