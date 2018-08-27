<template>
<div>
  <div id="person">
    <div class="tool-bar">
      <div class="logo">
        <img src="../../assets/logo1.png" width="200%" height="100%">
      </div>
      <table align="right">
        <tr>
          <td>
            <el-button
              class="user-ope"
              type="text"
              @click="logout">登出
            </el-button>
          </td>
        </tr>
      </table>
    </div>
  </div>
  <div id="person" class="hidden-sm-and-down">
    <el-container class="first-container">
      <el-aside>
        <el-menu
          :default-openeds="['5']"
          default-active="1"
          class="el-menu-vertical-demo"
          @select="handleSelect"
          :collapse="false">
          <el-submenu index="5">
            <template class="head" slot="title">
              <i class="el-icon-message"></i>
              <span slot="title">个人中心</span>
            </template>
            <el-menu-item class="col" index="1">浏览历史</el-menu-item>
            <el-menu-item class="col" index="2">订单列表</el-menu-item>
            <el-menu-item class="col" index="3">已购课程</el-menu-item>
            <el-menu-item class="col" index="4">个人信息</el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </div>

  <div id="person-mini" class="hidden-md-and-up">
    <el-container class="first-container">
      <el-aside>
        <el-menu
          :default-openeds="['5']"
          default-active="1"
          class="el-menu-vertical-demo"
          @select="handleSelect"
          :collapse="true">
          <el-submenu index="5">
            <template class="head" slot="title">
              <i class="el-icon-message"></i>
              <span slot="title">个人中心</span>
            </template>
            <el-menu-item class="col" index="1">浏览历史</el-menu-item>
            <el-menu-item class="col" index="2">订单列表</el-menu-item>
            <el-menu-item class="col" index="3">已购课程</el-menu-item>
            <el-menu-item class="col" index="4">个人信息</el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </div>

</div>
</template>
<script>
export default {
  data() {
    return {
    }
  },
  methods: {
    logout: function() {
    },
    handleSelect: function(key, keyPath) {
      switch (key) {
        case '1':
          this.$router.push('/brows')
          break
        case '2':
          this.$router.push('/userorder')
          break
        case '3':
          this.$router.push('/payeds')
          break
        case '4':
          this.$router.push('/personalinfor')
          break
      }
    }
  }
}
</script>
<style scoped>
  .tool-bar {
    width: 100%;
    max-height: 50px;
    margin: 0;
    padding: 0;
    background-color:lightskyblue;
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

  .el-aside {
    width: 250px !important;
    margin-left: 0px;
  }
  li {
     background-color: rgb(248, 248, 247);
  }
  .col {
    height: 60px !important;
    background-color:white;
  }
  .el-submenu__title {
    height: 60px !important;
    line-height:60px !important;
    background-color: rgb(238, 243, 247);
    font-size: 18px;
    vertical-align:middle;
    font-weight: bold;
  }

  .first-container {
    text-align: center;
    margin: 0px auto;
    width: 100%;
  }

  @media screen and (max-width: 800px) {
    .user-ope {
      color: black;
      font-size: 15px;
      margin-right: 10px;
    }
    .tool-bar {
      min-height: 42px;
    }
    .logo {
      margin-left: 30px;
      display: inline-block;
      width: 42px;
      height: 42px;
    }
    .el-aside {
      width: 65px !important;
      margin-left: 0px;
    }
    .first-container {
      text-align: center;
      margin: 0px auto;
      width: 100%;
    }
  }
</style>
