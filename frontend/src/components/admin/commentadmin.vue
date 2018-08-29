<template>
  <div class="first-div">
    <el-form  class="first-form"
      :label-position="labelPosition"
      :inline="true"
      label-width="100px"
      :model="commentMsg"
      :rules="rules"
      ref="commentMsg">
      <el-form-item label="课程编号" class="info-text" prop="courseId">
        <el-input v-model="commentMsg.courseId" class="info"></el-input>
      </el-form-item>
      <el-form-item label="用户账号" class="info-text" prop="phoneNumber">
        <el-input v-model="commentMsg.phoneNumber" class="info"></el-input>
      </el-form-item>
      <el-form-item class="info-text">
        <el-button type="primary" @click="onSubmitConfirm">
          搜索
        </el-button>
      </el-form-item>
    </el-form>
    <el-table
      border
      :data="post">
      <el-table-column
        header-align=center
        prop="courseId"
        label="课程编号"
        width="100px">
      </el-table-column>
      <el-table-column
        header-align=center
        prop="userName"
        label="用户昵称"
        width="150px">
      </el-table-column>
      <el-table-column
        header-align=center
        prop="phoneNumber"
        label="用户账号"
        width="120px">
      </el-table-column>
      <el-table-column
        header-align=center
        prop="msgContent"
        label="留言内容"
        width="250px">
      </el-table-column>
      <el-table-column
        header-align=center
        prop="createdAt"
        label="留言时间"
        width="150px">
      </el-table-column>
      <el-table-column
        header-align=center
        label="操作">
        <template slot-scope="scope">
          <el-button
            @click.native.prevent="deleteMsg(scope.$index)"
            type="text"
            size="small">
            删除
          </el-button>
          <el-button
            @click.native.prevent="forbidUser(scope.$index)"
            type="text"
            size="small">
            禁言
            </el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>
<script>
import * as utils from '../utils/utils.js'
import axios from 'axios'
import qs from 'qs'

export default {
  data() {
    var idReg = /^[0-9]*$/
    var phoneReg = /^1[3|4|5|7|8][0-9]\d{8}$/
    var validateCourse = (rule, value, callback) => {
      if (!idReg.test(value)) {
        return callback(new Error('课程序列格式不正确'))
      }
      callback()
    }
    var validatePhone = (rule, value, callback) => {
      if (!phoneReg.test(value) && value) {
        return callback(new Error('用户手机号码格式不正确'))
      }
      callback()
    }
    return {
      labelPosition: 'right',
      commentMsg: {
        courseId: '',
        phoneNumber: ''
      },
      post: [
        {
          id: 11111,
          courseId: '135156',
          phoneNumber: '13600000000',
          userName: 'UJoe',
          userId: 5443,
          msgContent: 'just a test. '
        },
        {
          id: 2222,
          courseId: '135156',
          phoneNumber: '13600000000',
          userName: 'UJoe',
          userId: 89088,
          msgContent: '在十九课里，我们学到了赵州桥是多么的雄伟、壮观。'
        }
      ],
      rules: {
        courseId: [{ validator: validateCourse, trigger: 'blur' }],
        phoneNumber: [{ validator: validatePhone, trigger: 'blur' }]
      }
    }
  },
  methods: {
    onSubmitConfirm: function() {
      axios.post(utils.getURL() + 'api/showmessage/', qs.stringify({
        courseId: this.commentMsg.courseId,
        clientId: this.commentMsg.phoneNumber
      })).then(response => {
        this.post = response.data.query
      })
    },
    onSubmitClearCourse: function() {
      this.commentMsg.courseId = ''
    },
    onSubmitClearPhone: function() {
      this.commentMsg.phoneNumber = ''
    },
    deleteMsg: function(index) {
      let msgId = this.post[index].id
      axios.post(utils.getURL() + 'api/deletemsg/', qs.stringify({
        msgId: msgId
      })).then(response => {
        let status = response.data.status
        if (status === 0) {
          this.$message.error('已禁言')
        } else {
          this.$message.error('信息有误！')
        }
      })
    },
    forbidUser: function(index) {
      let userId = this.post[index].userId
      axios.post(utils.getURL() + 'api/shutup/', qs.stringify({
        userId: userId
      })).then(response => {
        let status = response.data.status
        if (status === 0) {
          this.$message.error('已禁言')
        } else {
          this.$message.error('用户信息有误！')
        }
      })
    }
  },
  created: function() {
    axios.post(utils.getURL() + 'api/showmessage/').then(response => {
      this.post = response.data.query
    })
  }
}
</script>
<style scoped>
  .first-div {
    width: 80%;
    margin: 50px auto;
    text-align: center;
  }
  .first-form {
    margin-bottom: 50px !important;
  }
</style>
