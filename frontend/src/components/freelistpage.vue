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

</style>
