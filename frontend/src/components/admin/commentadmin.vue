<template>
  <div class="firstdiv">
    <el-form  class="firstform" :label-position="labelPosition" :inline="true" label-width="100px" :model="commentMsg" :rules="rules" ref="commentMsg">
      <el-form-item label="课程编号" class="infor_text" prop="courseId">
        <el-input v-model="commentMsg.courseId" class="infor"></el-input>
      </el-form-item>
      <el-form-item label="用户账号" class="infor_text" prop="phoneNumber">
        <el-input v-model="commentMsg.phoneNumber" class="infor"></el-input>
      </el-form-item>
      <el-form-item class="infor_text">
        <el-button type="primary" @click="onSubmitConfirm('commentMsg')">搜索</el-button>
      </el-form-item>
    </el-form>
    <el-table
      border
      :data="post">
      <el-table-column
        header-align=center
        prop="courseId"
        label="课程编号"
        width="150">
      </el-table-column>
      <el-table-column
        header-align=center
        prop="userName"
        label="用户昵称"
        width="150">
      </el-table-column>
      <el-table-column
        header-align=center
        prop="phoneNumber"
        label="用户账号"
        width="150">
      </el-table-column>
      <el-table-column
        header-align=center
        prop="msgContent"
        label="留言内容"
        width="300">
      </el-table-column>
      <el-table-column
        header-align=center
        label="操作">
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
  </div>
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
        {
          courseId: '135156',
          phoneNumber: '13600000000',
          userName: 'UJoe',
          msgContent: 'just a test. '
        },
        {
          courseId: '135156',
          phoneNumber: '13600000000',
          userName: 'UJoe',
          msgContent: 'just a test. 在十九课里，我们学到了赵州桥是多么的雄伟、壮观。'
        }
      ],
      rules: {
        courseId: [{ validator: validateCourse, trigger: 'blur' }],
        phoneNumber: [{ validator: validatePhone, trigger: 'blur' }]
      }
    }
  },
  methods: {
    onSubmitConfirm(commentMsg) {
      this.$refs[commentMsg].validate(valid => {
        if (valid) {
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
    },
    forbidUser() {
    }
  }
}
</script>
<style scoped>
  .firstdiv {
  width: 1000px;
  margin: 50px auto;
  text-align: center;
}

  .firstform {
  margin-bottom: 50px !important;
}
</style>
