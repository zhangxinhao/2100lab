<template>
    <div>
        <el-container>
            <el-header>
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
            </el-header>
        </el-container>
    </div>
</template>

<script>
export default {};
</script>

<style>
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
  </style>
