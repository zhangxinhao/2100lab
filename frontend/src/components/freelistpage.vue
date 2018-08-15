<template>
<div class="freelist">

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

  <div class="menu">
    <ul>
      <li style="display:inline">
        <router-link to="/">
          <el-button icon="el-icon-back">首页</el-button>
        </router-link>
      </li>
      <li style="display:inline">
        <el-button type="primary" disabled>免费区</el-button>
      </li>
      <li style="display:inline">
        <el-button>付费区</el-button>
      </li>
    </ul>
  </div>
</div>

</template>

<script>
export default {
  data() {
    return {
      login: true,
      not_login: false
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

  .freelist {
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
  li, ul {
    list-style: none;
  }
  .menu {
    position: relative;
    height: 50px;
    margin: 0, auto;
    padding: 8px 0 0;
    margin-top: 10px;
    margin-bottom: 50px;
    z-index: 99;
    border-bottom: 1px, solid, black;
  }
</style>
