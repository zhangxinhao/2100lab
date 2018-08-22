<template>
  <el-form class="main_form">
    <el-form-item>
      <el-col class="personalinfor_header">
        <img :src="header" class="header_img">
      </el-col>
    </el-form-item>
    <el-button @click="dialogVisible = true" class="change_header" type="text">修改头像</el-button>
    <el-dialog
      title="更换头像"
      :visible.sync="dialogVisible"
      width="25%"
      :before-close="handleClose">
      <span class="dialog_msg">请上传头像</span>
      <el-upload
        class="avatar-uploader"
        action=""
        :show-file-list="false"
        :on-success="handleAvatarSuccess"
        :before-upload="beforeAvatarUpload">
        <img v-if="imageUrl" :src="imageUrl" class="avatar">
        <i v-else class="el-icon-plus avatar-uploader-icon"></i>
      </el-upload>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="clickToChangeIcon">确 定</el-button>
      </span>
    </el-dialog>
    <el-form :label-position="labelPosition" label-width="80px" :model="userMsg">
      <el-form-item label="认证用户" v-if="userMsg.is_V" class="V"></el-form-item>
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
import * as utils from '../utils/utils.js'

export default {
  data() {
    return {
      header: require('../../assets/images/header2.jpg'),
      labelPosition: 'right',
      userMsg: {
        name: 'UJoe',
        phonenumber: '13600000000',
        balance: '1123',
        is_V: true
      },
      dialogVisible: false,
      imageUrl: ''
    }
  },
  methods: {
    onSubmitConfirm() {
      axios.post(utils.getURL() + 'api/setalias/', qs.stringify({
        newAlias: this.userMsg.name
      })).then(
        response => {
          alert(response.data.result)
        }
      )
    },
    clickToChangeIcon() {
      this.dialogVisible = false
      this.header = require('../../assets/images/header1.jpg')
    },
    handleAvatarSuccess(res, file) {
      this.imageUrl = URL.createObjectURL(file.raw)
    },
    beforeAvatarUpload(file) {
      const isJPG = file.type === 'image/jpeg'
      const isLt2M = file.size / 1024 / 1024 < 2

      if (!isJPG) {
        this.$message.error('上传头像图片只能是 JPG 格式!')
      }
      if (!isLt2M) {
        this.$message.error('上传头像图片大小不能超过 2MB!')
      }
      return isJPG && isLt2M
    },
    handleClose(done) {
      this.$confirm('确认关闭？你的编辑在离开网页时将会丢失！')
        .then(_ => {
          done()
        })
        .catch(_ => {})
    }
  },
  mounted: function() {
    axios.post(utils.getURL() + 'api/getuserinfo/').then(
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
    margin-left: 32%;
  }

  .dialog_msg {
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

  .personalinfor_describelable {
    float: left;
    width: 80px;
    margin-top: 80px;
  }

  .V {
    margin-left: 31%;
  }

  .infor {
    width: 33%;
  }

  .infor_text {
    margin-left:16%;
  }
</style>
