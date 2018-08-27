<template>
  <div class="out-div">
    <div class="toolbar">
      <div class="logo">
      <img src="../../assets/logo2.png" width="200%" height="100%">
      </div>
      <table align="right">
        <tr>
          <td>
            <el-button class="user-ope" type="text" @click="logout">登出</el-button>
          </td>
        </tr>
      </table>
    </div>
    <el-container class="admin-first">
      <el-container class="admin-second">
        <el-aside class="admin-aside">
          <el-menu @select="handleSelect" unique-opened:false >
            <el-submenu index="1" v-if="authorizationList.courseManage">
              <template class="first-bar" slot="title"><i class="el-icon-edit"></i>课程管理</template>
              <el-menu-item class="col" index="1-1">课程上传</el-menu-item>
              <el-menu-item class="col" index="1-2">课程编辑</el-menu-item>
            </el-submenu>
            <el-submenu index="2" v-if="authorizationList.userManage">
              <template class="second-bar" slot="title"><i class="el-icon-document"></i>管理用户</template>
              <el-menu-item class="col" index="2-1">用户信息</el-menu-item>
              <el-menu-item class="col" index="2-2">用户浏览</el-menu-item>
              <el-menu-item class="col" index="2-3">留言管理</el-menu-item>
            </el-submenu>
            <el-submenu index="3" v-if="authorizationList.operationHistory">
              <template class="second-bar" slot="title"><i class="el-icon-date"></i>操作历史</template>
              <el-menu-item class="col" index="3-1">后台操作历史</el-menu-item>
            </el-submenu>
             <el-submenu index="4" v-if="authorizationList.orderManage">
              <template class="second-bar" slot="title"><i class="el-icon-news"></i>订单管理</template>
              <el-menu-item class="col" index="4-1">用户订单</el-menu-item>
            </el-submenu>
             <el-submenu index="5">
              <template class="second-bar" slot="title"><i class="el-icon-view"></i>数据统计</template>
              <el-menu-item class="col" index="5-1">数据分析</el-menu-item>
            </el-submenu>
             <el-submenu index="6" v-if="authorizationList.adminManage">
              <template class="second-bar" slot="title"><i class="el-icon-plus"></i>管理员操作</template>
              <el-menu-item class="col" index="6-1">新增管理员</el-menu-item>
              <el-menu-item class="col" index="6-2">编辑管理员</el-menu-item>
            </el-submenu>
          </el-menu>
        </el-aside>
        <el-main>
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import axios from 'axios'
import * as utils from '../utils/utils.js'

export default {
  data() {
    return {
      authorizationList: {
        courseManage: true,
        userManage: true,
        operationHistory: true,
        orderManage: true,
        adminManage: true
      }
    }
  },
  methods: {
    logout: function() {
      axios.post(utils.getURL() + 'api/logout/').then(response => {
        if (response.data.status === 0) {
          this.$router.push('/adminlogin')
        }
      })
    },
    handleSelect(key, keyPath) {
      switch (key) {
        case '1-1':
          this.$router.push('/uploadCourse')
          break
        case '1-2':
          this.$router.push('/courseManage')
          break
        case '2-1':
          this.$router.push('/usermanage')
          break
        case '2-2':
          this.$router.push('/userBrowsing')
          break
        case '2-3':
          this.$router.push('/commentadmin')
          break
        case '3-1':
          this.$router.push('/adminHistory')
          break
        case '4-1':
          this.$router.push('/orderAdmin')
          break
        case '5-1':
          this.$router.push('/dataAnalize')
          break
        case '6-1':
          this.$router.push('/addAdmin')
          break
        case '6-2':
          this.$router.push('/adminManage')
          break
      }
    }
  },
  created: function() {
    axios.post(utils.getURL() + 'api/authorizationcheck/').then(response => {
      this.authorizationList = response.data.rights
    })
  }
}
</script>
<style scoped>
  .el-aside {
    width: 15% !important;
    margin-left: 0px;
  }
  .toolbar {
    width: 100%;
    min-height: 50px;
    margin: 0;
    padding: 0;
    background-color: #606266;
    opacity: 0.7;
  }

  .logo {
    margin-left: 50px;
    display: inline-block;
    width: 50px;
    height: 50px;
  }

  .user-ope {
    color: black;
    font-size:18px;
    margin-right: 60px;
  }
  .admin-first {
    /* width: 1600px; */
    margin: 0px auto 0px auto;
    text-align: center;
    color: white;
  }
  .el-submenu__title {
    height: 60px !important;
    line-height:60px !important;
    background-color: white;
    font-size: 18px;
    vertical-align: middle;
    font-weight: bold;
  }
  .col {
    height: 60px;
    min-width: 100px !important;
  }

  li {
    background-color: rgb(248, 248, 247);
  }
  li:hover {
    background-color: white !important;
  }
  .col {
    min-width: 100px !important;
  }
</style>
