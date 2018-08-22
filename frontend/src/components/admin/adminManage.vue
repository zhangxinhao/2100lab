<template>
<div class="admin-manage">

  <div id="search-admin">
    <el-row :gutter="20">
      <el-col :span="6" :offset="14"><el-input v-model="search_adminId" placeholder="请输入管理员ID"></el-input></el-col>
      <el-col :span="2"><el-button type="primary" icon="el-icon-search">搜索</el-button></el-col>
    </el-row>
  </div>

  <div id="admin-list">
    <el-table :data="adminData" border width=100%>
      <el-table-column type="index" :index="indexMethod" header-align=center></el-table-column>
      <el-table-column prop="adminId" label="管理员编号" width="150" header-align=center></el-table-column>
      <el-table-column prop="course_manage" label="课程管理" width="150" header-align=center :formatter="courseRightCal" show-overflow-tooltip></el-table-column>
      <el-table-column prop="user_manage" label="用户管理" width="150" header-align=center :formatter="userRightCal" show-overflow-tooltip></el-table-column>
      <el-table-column prop="operation_history" label="操作历史" width="150" header-align=center :formatter="historyRightCal" show-overflow-tooltip></el-table-column>
      <el-table-column prop="order_manage" label="订单管理" width="150" header-align=center :formatter="orderRightCal" show-overflow-tooltip></el-table-column>
      <el-table-column prop="admin_manage" label="添加管理员" width="150" header-align=center :formatter="adminRightCal" show-overflow-tooltip></el-table-column>
      <el-table-column label="操作" header-align=center>
        <template slot-scope="scope">
          <el-button type="text" size="small" @click="editFunction(scope.$index)">编辑</el-button>
          <el-button type="text" size="small" @click="deleteFunction(scope.$index)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>

  <div class="editdialog">
    <el-dialog title="编辑管理员" :visible.sync="editVisible" width="400px">
      <el-form>
        <el-form-item label="管理员编号">
          <el-input v-model="adminData[editIndex].adminId" class="inp" readonly></el-input>
        </el-form-item>

        <el-form-item label="管理员密码">
          <el-input v-model="adminData[editIndex].password" class="inp" placeholder="为空默认为原密码"></el-input>
        </el-form-item>

        <el-form-item label="课程管理权限">
          <el-switch v-model="adminData[editIndex].course_manage"></el-switch>
        </el-form-item>

        <el-form-item label="用户管理权限">
          <el-switch v-model="adminData[editIndex].user_manage"></el-switch>
        </el-form-item>

        <el-form-item label="操作历史权限">
          <el-switch v-model="adminData[editIndex].operation_history"></el-switch>
        </el-form-item>

        <el-form-item label="订单管理权限">
          <el-switch v-model="adminData[editIndex].order_manage"></el-switch>
        </el-form-item>

      </el-form>
      <div slot="footer" class="edit-footer">
        <el-button @click="editCancel">取 消</el-button>
        <el-button type="primary" @click="edit">确 定</el-button>
      </div>
    </el-dialog>
  </div>

  <div class="deletedialog">
    <el-dialog title="删除管理员" :visible.sync="deleteVisible" width="400px" height="700px">
      <div>确认要删除编号为：{{adminData[editIndex].adminId}} 的用户？</div>
      <div slot="footer" class="edit-footer">
        <el-button @click="deleteCancel">取 消</el-button>
        <el-button type="primary" @click="deleteIt">确 定</el-button>
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
      search_adminId: '',
      index: 0,
      editIndex: 0,
      editVisible: false,
      deleteIndex: 0,
      deleteVisible: false,
      adminData: [
        {adminId: '001', password: '123456', course_manage: true, user_manage: true, operation_history: true, order_manage: true, admin_manage: true},
        {adminId: '122', password: '111111', course_manage: false, user_manage: true, operation_history: true, order_manage: false, admin_manage: false}
      ]
    }
  },
  methods: {
    indexMethod(index) {
      return index + 1
    },
    editFunction(editIndex) {
      this.editVisible = true
      this.editIndex = editIndex
    },
    edit() {
      this.editVisible = false
      let admin = this.adminData[this.editIndex]
      let password
      if (admin.password !== '') {
        password = hash.getHash(admin.password)
      }
      axios.post(utils.getURL() + 'api/editadmin/', qs.stringify({
        adminId: admin.adminId,
        password: password,
        course_manage: admin.course_manage,
        user_manage: admin.user_manage,
        operation_history: admin.operation_history,
        order_manage: admin.order_manage
      })).then(response => {
        if (response.data.status === 0) {
          alert('编辑成功')
        } else {
          alert('编辑失败')
        }
      })
    },
    deleteFunction(deleteIndex) {
      this.deleteVisible = true
      this.deleteIndex = deleteIndex
    },
    deleteIt() {
      this.deleteVisible = false
      axios.post(utils.getURL() + 'api/deleteadmin/', qs.stringify({
        adminId: this.adminData[this.editIndex].adminId
      })).then(response => {
        if (response.data.status === 0) {
          alert('已删除')
        } else {
          alert('删除失败')
        }
      })
    },
    courseRightCal(data) {
      return data.course_manage ? '开放' : '关闭'
    },
    userRightCal(data) {
      return data.user_manage ? '开放' : '关闭'
    },
    historyRightCal(data) {
      return data.operation_history ? '开放' : '关闭'
    },
    orderRightCal(data) {
      return data.order_manage ? '开放' : '关闭'
    },
    adminRightCal(data) {
      return data.admin_manage ? '开放' : '关闭'
    },
    editCancel() {
      this.editVisible = false
    },
    deleteCancel() {
      this.deleteVisible = false
    },
    search() {
      axios.post(utils.getURL() + 'api/getadmin/', qs.stringify({
        adminId: this.search_adminId
      })).then(response => {
        if (response.data.status === 0) {
          this.adminData = response.data.admins
        } else {
          alert('查询错误！')
        }
      })
    }
  },
  created: function() {
    axios.post(utils.getURL() + 'api/getadmin/').then(response => {
      if (response.data.status === 0) {
        this.adminData = response.data.admins
      } else {
        alert('查询错误！')
      }
    })
  }
}
</script>

<style scoped>
.admin-manage {
  width: 1300px;
  margin: 20px auto;
}
#search-admin {
  width: 1280px;
}
#admin-list {
  width: 1100px;
  height: 1000px;
  margin: 50px auto;
  text-align: center;
}
</style>
