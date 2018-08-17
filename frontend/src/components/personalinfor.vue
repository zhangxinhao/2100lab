<template>
  <el-form class="main_form">
    <el-form-item>
      <el-col class="personalinfor_header">
        <img :src="header" class="header_img">
      </el-col>
    </el-form-item>
    <router-link to="" class="change_header">修改头像</router-link>
    <div class="input_block"></div>
    <el-form :label-position="labelPosition" label-width="80px" :model="userMsg">
      <el-form-item label="认证用户" v-if="userMsg.is_V" class="is_V"></el-form-item>
      <el-form-item label="用户名" class="infor_text">
        <el-input v-model="userMsg.name" class="infor"></el-input>
      </el-form-item>
      <el-form-item label="手机号码" class="infor_text">
        <el-input v-model="userMsg.phonenumber" class="infor" :disabled="true"></el-input>
      </el-form-item>
      <el-form-item label="赏金" class="infor_text">
        <el-input v-model="userMsg.balance" class="infor" :disabled="true"></el-input>
      </el-form-item>
      <el-form-item class="infor_text">
        <el-button type="primary" @click="onSubmitConfirm">确认修改</el-button>
      </el-form-item>
    </el-form>
  </el-form>
</template>
<script>
import qs from 'qs'
import axios from 'axios'
export default {
  data() {
    return {
      header: require('../assets/images/header2.jpg'),
      labelPosition: 'right',
      userMsg: {
        name: 'UJoe',
        phonenumber: '13600000000',
        balance: '1123',
        is_V: true
      }
    }
  },
  methods: {
    onSubmitConfirm() {
      axios.post('http://192.168.55.33:8000/api/setalias/', qs.stringify({
        newAlias: this.userMsg.name
      })).then(
        response => {
          alert(response.data.result)
        }
      )
    },
    clickToChangeIcon() {
      axios.post('http://192.168.55.33:8000/api/seticon/').then(
        response => {
          alert(response.data.result)
        }
      )
    }
  },
  mounted: function() {
    axios.post('http://192.168.55.33:8000/api/getuserinfo/').then(
      response => {
        this.userMsg.name = response.data
      }
    )
  }
}
</script>
<style scoped>
  .personalinfor_header {
    width: 100px;
    height: 100px;
    overflow: hidden;
    margin-left: 30%;
    border: 3px solid skyblue;
  }

  .main_form {
    text-align: left;
    margin-left: 10%;
  }

  .header_img {
    width: 100%;
    height: 100%;
    object-fit: fill;
  }

  .change_header {
    margin-left: 31.5%;
  }

  .input_block {
    margin: 20px;
  }

  .personalinfor_describelable {
    float: left;
    width: 80px;
    margin-top: 80px;
  }

  .is_V {
    color: red !important;
    margin-left: 31%;
  }

  .infor {
    width: 33%;
  }

  .infor_text {
    margin-left:16%;
  }
</style>
