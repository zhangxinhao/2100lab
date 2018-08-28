<template>
  <el-form class="main-form">
    <el-form-item>
      <el-col class="personalinfor-header">
        <img :src="header" class="header-img">
      </el-col>
    </el-form-item>
    <el-button
      @click="dialogVisible = true"
      class="change-header"
      type="text">修改头像
    </el-button>
    <el-dialog
      title="更换头像"
      width="300px"
      :visible.sync="dialogVisible">
      <span class="dialog-msg">请上传头像</span>
      <el-upload
        class="avatar-uploader"
        :action="uploadURL()"
        :data="userMsg"
        :show-file-list="false"
        :on-success="handleAvatarSuccess"
        :before-upload="beforeAvatarUpload">
        <img v-if="imageUrl" :src="imageUrl" class="avatar">
        <i v-else class="el-icon-plus avatar-uploader-icon"></i>
      </el-upload>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="clickToChangeIcon">
          确 定
        </el-button>
      </span>
    </el-dialog>
    <el-form :label-position="labelPosition"
      label-width="80px"
      :model="userMsg">
      <el-form-item label="认证用户" v-if="userMsg.isV" class="V">
      </el-form-item>
      <el-form-item label="用户名" class="infor-text">
        <el-input v-model="userMsg.name" class="infor"></el-input>
      </el-form-item>
      <el-form-item label="手机号码" class="infor-text">
        <el-input
          v-model="userMsg.phoneNumber"
          class="infor"
          :disabled="true">
        </el-input>
      </el-form-item>
      <el-form-item label="赏金" class="infor-text">
        <el-input
          v-model="userMsg.balance"
          class="infor"
          :disabled="true">
        </el-input>
      </el-form-item>
      <el-form-item class="infor-text">
        <el-button type="primary" @click="onSubmitConfirm">
          确认修改
        </el-button>
      </el-form-item>
    </el-form>
  </el-form>
</template>

<script>
import qs from 'qs'
import axios from 'axios'
import * as utils from '../utils/utils.js'

export default {
  data() {
    return {
      header: require('../../assets/images/header2.jpg'),
      labelPosition: 'right',
      userMsg: {
        name: 'UJoe',
        phoneNumber: '13230037688',
        balance: '1123',
        isV: true
      },
      dialogVisible: false,
      imageUrl: ''
    }
  },
  methods: {
    uploadURL: function() {
      return utils.getURL() + 'api/seticon/'
    },
    onSubmitConfirm: function() {
      axios.post(utils.getURL() + 'api/setalias/', qs.stringify({
        newAlias: this.userMsg.name,
        phonenumber: this.userMsg.phoneNumber
      })).then(
        response => {
        }
      )
    },
    clickToChangeIcon: function() {
      this.dialogVisible = false
      this.header = this.imageUrl
    },
    handleAvatarSuccess: function(res, file) {
      this.imageUrl = URL.createObjectURL(file.raw)
    },
    beforeAvatarUpload: function(file) {
      const isJPG = file.type === 'image/jpeg'
      const isLt2M = file.size / 1024 / 1024 < 2

      if (!isJPG) {
        this.$message.error('上传头像图片只能是 JPG 格式!')
      }
      if (!isLt2M) {
        this.$message.error('上传头像图片大小不能超过 2MB!')
      }
      return isJPG && isLt2M
    }
  },
  created: function() {
    axios.post(utils.getURL() + 'api/getuserinfo/', qs.stringify({
    })).then(response => {
      this.header = utils.getURL() + 'media/' +
        response.data.list[0].fields.icon
      this.userMsg.name = response.data.list[0].fields.alias
      this.userMsg.phoneNumber = response.data.list[0].fields.username
      this.userMsg.balance = response.data.list[0].fields.balance
      this.userMsg.isV = response.data.list[0].fields.is_v
    })
  }
}
</script>
<style scoped>
  .personalinfor-header {
    width: 100px;
    height: 100px;
    overflow: hidden;
    margin-left: 30%;
    border: 3px solid skyblue;
  }

  .main-form {
    text-align: left;
    margin-left: 10%;
  }

  .header-img {
    width: 100%;
    height: 100%;
    object-fit: fill;
  }

  .change-header {
    margin-left: 32%;
  }

  .dialog-msg {
    margin-left: 5%;
  }

  .avatar-uploader {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
    width: 120px;
    height: 120px;
    margin-left: 32%;
  }

  .avatar-uploader:hover {
    border-color: #409EFF;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 120px;
    height: 120px;
    line-height: 120px;
  }
  .avatar {
    width: 120px;
    height: 120px;
    display: block;
  }

  .V {
    margin-left: 30%;
  }

  .infor {
    width: 33%;
  }

  .infor-text {
    margin-left: 16%;
  }
  .el-dialog {
    width: 25%;
  }
  @media screen and (max-width: 500px) {
  .V {
    margin-left: 30%;
  }

  .infor {
    width: 70%;
  }

  .infor-text {
    margin-left: 0px;
  }
  .el-dialog {
    width: 100%;
    height: 100px !important;
  }
}
</style>
