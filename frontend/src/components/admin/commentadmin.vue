<template>
  <el-container>
    <el-header style="text-align: center;">
      留言管理
      <hr>
    </el-header>
    <el-main>
      <el-form style="text-align: left; margin-left: 10%;">
        <div style="margin: 20px;"></div>
        <el-form :label-position="labelPosition" label-width="100px" :model="commentMsg" :rules="rules" ref="commentMsg" class="demo-ruleForm">
          <el-form-item label="课程序列" class="infor_text" prop="courseId">
            <el-input v-model="commentMsg.courseId" class="infor"></el-input>
            <el-button @click="onSubmitClearCourse" style="margin-left:3%;">清空</el-button>
          </el-form-item>
          <el-form-item label="用户手机号码" class="infor_text" prop="phoneNumber">
            <el-input v-model="commentMsg.phoneNumber" class="infor"></el-input>
            <el-button @click="onSubmitClearPhone" style="margin-left:3%;">清空</el-button>
          </el-form-item>
          <el-form-item class="infor_text">
            <el-button type="primary" @click="onSubmitConfirm('commentMsg')" style="margin-left:15%;">搜索</el-button>
          </el-form-item>
        </el-form>
        <div style="margin: 20px;"></div>
        <el-form>
          <el-table
            :data="post"
            style="width: 80%"
            max-height="500">
            <el-table-column
              fixed
              prop="courseId"
              label="课程序列"
              width="150">
            </el-table-column>
            <el-table-column
              prop="userName"
              label="用户名"
              width="150">
            </el-table-column>
            <el-table-column
              prop="phoneNumber"
              label="用户手机号码"
              width="150">
            </el-table-column>
            <el-table-column
              prop="msgContent"
              label="留言内容"
              width="300">
            </el-table-column>
            <el-table-column
              fixed="right"
              label="操作"
              width="120">
              <template slot-scope="scope">
                <el-button
                  @click.native.prevent="deleteMsg"
                  type="text"
                  size="small">
                  删除
                </el-button>
                <el-button
                  @click.native.prevent="forbidUser"
                  type="text"
                  size="small">
                  禁言
                </el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-form>
      </el-form>
    </el-main>
  </el-container>
</template>
<script>
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
        {courseId: '135156', phoneNumber: '13600000000', userName: 'UJoe', msgContent: 'just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. just a test. '}
      ],
      rules: {
        courseId: [{validator: validateCourse, trigger: 'blur'}],
        phoneNumber: [{validator: validatePhone, trigger: 'blur'}]
      }
    }
  },
  methods: {
    onSubmitConfirm(commentMsg) {
      this.$refs[commentMsg].validate((valid) => {
        if (valid) {
          alert('submit!')
        } else {
          return false
        }
      })
    },
    onSubmitClearCourse() {
      this.commentMsg.courseId = ''
    },
    onSubmitClearPhone() {
      this.commentMsg.phoneNumber = ''
    },
    deleteMsg() {
      alert('delete!')
    },
    forbidUser() {
      alert('forbid!')
    }
  }
}
</script>
<style scoped>

  .infor {
    width: 33%;
  }

  .infor_text {
    margin-left:16%;
  }
</style>
