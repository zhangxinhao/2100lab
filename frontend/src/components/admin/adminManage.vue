<template>
<div class="admin-manage">

  <div id="search-admin">
    <el-row :gutter="20">
      <el-col :span="6" :offset="14">
        <el-input v-model="searchAdminId" placeholder="请输入管理员ID">
        </el-input>
      </el-col>
      <el-col :span="2">
        <el-button type="primary" icon="el-icon-search" @click="search">
          搜索
        </el-button>
      </el-col>
    </el-row>
  </div>

  <div id="admin-list">
    <el-table :data="adminData" border>
      <el-table-column
        type="index"
        :index="indexMethod"
        header-align=center>
      </el-table-column>
      <el-table-column
        prop="adminId"
        label="管理员编号"
        width=120%
        header-align=center>
      </el-table-column>
      <el-table-column
        prop="courseManage"
        label="课程管理"
        width=100%
        header-align=center
        :formatter="courseRightCal"
        show-overflow-tooltip>
      </el-table-column>
      <el-table-column
        prop="userManage"
        label="用户管理"
        width=100%
        header-align=center
        :formatter="userRightCal"
        show-overflow-tooltip>
      </el-table-column>
      <el-table-column
        prop="operationHistory"
        label="操作历史"
        width=100%
        header-align=center
        :formatter="historyRightCal"
        show-overflow-tooltip>
      </el-table-column>
      <el-table-column
        prop="orderManage"
        label="订单管理"
        width=100%
        header-align=center
        :formatter="orderRightCal"
        show-overflow-tooltip>
      </el-table-column>
      <el-table-column
        prop="adminManage"
        label="添加管理员"
        width=100%
        header-align=center
        :formatter="adminRightCal"
        show-overflow-tooltip>
      </el-table-column>
      <el-table-column label="操作" header-align=center>
        <template slot-scope="scope">
          <el-button
            type="text"
            size="small"
            @click="editFunction(scope.$index)">
            编辑
          </el-button>
          <el-button
            type="text"
            size="small"
            @click="deleteFunction(scope.$index)">
            删除
          </el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>

  <div class="edit-dialog">
    <el-dialog
      title="编辑管理员"
      :visible.sync="editVisible"
      width="400px">
      <el-form>
        <el-form-item label="管理员编号">
          <el-input
            v-model="adminData[editIndex].adminId"
            class="inp"
            readonly>
          </el-input>
        </el-form-item>

        <el-form-item label="管理员密码">
          <el-input
            v-model="adminData[editIndex].password"
            class="inp"
            placeholder="为空默认为原密码">
          </el-input>
        </el-form-item>

        <el-form-item label="课程管理权限">
          <el-switch
            v-model="adminData[editIndex].courseManage">
          </el-switch>
        </el-form-item>

        <el-form-item label="用户管理权限">
          <el-switch v-model="adminData[editIndex].userManage">
          </el-switch>
        </el-form-item>

        <el-form-item label="操作历史权限">
          <el-switch v-model="adminData[editIndex].operationHistory">
          </el-switch>
        </el-form-item>

        <el-form-item label="订单管理权限">
          <el-switch v-model="adminData[editIndex].orderManage">
          </el-switch>
        </el-form-item>

      </el-form>
      <div slot="footer" class="edit-footer">
        <el-button type="primary" @click="editCancel">取 消</el-button>
        <el-button @click="edit">确 定</el-button>
      </div>
    </el-dialog>
  </div>

  <div class="delete-dialog">
    <el-dialog title="删除管理员"
      :visible.sync="deleteVisible"
      width="400px"
      height="700px">
      <div>确认要删除编号为：{{ adminData[editIndex].adminId }} 的用户？</div>
      <div slot="footer" class="edit-footer">
        <el-button type="primary" @click="deleteCancel">取 消</el-button>
        <el-button @click="deleteIt">确 定</el-button>
      </div>
    </el-dialog>
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
    return {
      searchAdminId: '',
      index: 0,
      editIndex: 0,
      editVisible: false,
      deleteIndex: 0,
      deleteVisible: false,
      adminData: [{
        adminId: '无',
        password: '',
        courseManage: false,
        userManage: false,
        operationHistory: false,
        orderManage: false,
        adminManage: false
      }],
      backup: {
        courseManage: true,
        userManage: true,
        operationHistory: true,
        orderManage: true
      }
    }
  },
  methods: {
    indexMethod: function(index) {
      return index + 1
    },
    editFunction: function(editIndex) {
      let admin = this.adminData[editIndex]
      if (admin.adminId !== '无') {
        this.editVisible = true
        this.editIndex = editIndex
        this.backup.courseManage = this.adminData[editIndex].courseManage
        this.backup.userManage = this.adminData[editIndex].userManage
        this.backup.operationHistory =
          this.adminData[editIndex].operationHistory
        this.backup.adminManage = this.adminData[editIndex].courseManage
      }
    },
    edit: function() {
      this.editVisible = false
      let admin = this.adminData[this.editIndex]
      if (admin.adminId !== '无') {
        let password
        if (admin.password !== '') {
          password = hash.getHash(admin.password)
        }
        axios.post(utils.getURL() + 'api/editadmin/', qs.stringify({
          adminId: admin.adminId,
          password: password,
          course_manage: admin.courseManage,
          user_manage: admin.userManage,
          operation_history: admin.operationHistory,
          order_manage: admin.orderManage
        })).then(response => {
          if (response.data.status === 0) {
            this.$message({
              message: '编辑成功',
              type: 'success'
            })
          } else {
            this.$message.error('编辑失败')
          }
        })
      }
    },
    deleteFunction: function(deleteIndex) {
      let admin = this.adminData[deleteIndex]
      if (admin.adminId === '无') {
        return
      }
      this.deleteVisible = true
      this.deleteIndex = deleteIndex
    },
    deleteIt: function() {
      this.deleteVisible = false
      let admin = this.adminData[this.editIndex]
      if (admin.adminId === '无') {
        return
      }
      axios.post(utils.getURL() + 'api/deleteadmin/', qs.stringify({
        adminId: admin.adminId
      })).then(response => {
        if (response.data.status === 0) {
          this.$message({
            message: '已删除',
            type: 'success'
          })
        } else {
          this.$message.error('删除失败')
        }
      })
    },
    courseRightCal: function(data) {
      return data.courseManage ? '开放' : '关闭'
    },
    userRightCal: function(data) {
      return data.userManage ? '开放' : '关闭'
    },
    historyRightCal: function(data) {
      return data.operationHistory ? '开放' : '关闭'
    },
    orderRightCal: function(data) {
      return data.orderManage ? '开放' : '关闭'
    },
    adminRightCal: function(data) {
      return data.adminManage ? '开放' : '关闭'
    },
    editCancel: function() {
      this.editVisible = false
      this.adminData[this.editIndex].courseManage = this.backup.courseManage
      this.adminData[this.editIndex].userManage = this.backup.userManage
      this.adminData[this.editIndex].operationHistory =
        this.backup.operationHistory
      this.adminData[this.editIndex].orderManage = this.backup.orderManage
    },
    deleteCancel: function() {
      this.deleteVisible = false
    },
    search: function() {
      axios.post(utils.getURL() + 'api/getadmin/', qs.stringify({
        adminId: this.searchAdminId
      })).then(response => {
        if (response.data.status === 0) {
          this.adminData = response.data.admins
        } else {
          this.adminData = [{
            adminId: '无',
            password: '',
            courseManage: false,
            userManage: false,
            operationHistory: false,
            orderManage: false,
            adminManage: false
          }]
          this.$message.error('查询错误！')
        }
      })
    }
  },
  created: function() {
    axios.post(utils.getURL() + 'api/getadmin/').then(response => {
      if (response.data.status === 0) {
        this.adminData = response.data.admins
      } else {
        this.$message.error('查询错误！')
      }
    })
  }
}
</script>

<style scoped>
.admin-manage {
  width: 70%;
  margin: 20px 5%;
}
#search-admin {
  width: 100%;
}
#admin-list {
  width: 100%;
  min-height: 1000px;
  margin: 50px auto;
  text-align: center;
}
</style>
