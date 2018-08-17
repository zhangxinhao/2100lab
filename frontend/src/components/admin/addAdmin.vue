<template>
  <div class="addAdmin">
    <el-form ref="newAdmin"
      :model="newAdmin"
      label-width="200px" >

      <el-form-item label="管理员编号"  >
        <el-input v-model="newAdmin.adminName" class="inp"></el-input>
      </el-form-item>

      <el-form-item label="管理员密码" >
        <el-input v-model="newAdmin.adminKey" class="inp"></el-input>
      </el-form-item>

      <el-form-item label="课程管理权限">
        <el-switch v-model="newAdmin.courseManege" active-value="true" inactive-value="false"></el-switch>
      </el-form-item>

      <el-form-item label="管理用户权限" >
        <el-switch v-model="newAdmin.userManege" active-value="true" inactive-value="false"></el-switch>
      </el-form-item>

      <el-form-item label="操作历史权限">
        <el-switch v-model="newAdmin.historyManage" active-value="true" inactive-value="false" @change="newv"></el-switch>
      </el-form-item>

      <el-form-item label="订单管理权限">
        <el-switch v-model="newAdmin.orderManege" active-value="true" inactive-value="false"></el-switch>
      </el-form-item>

      <el-form-item label="添加管理员权限">
        <el-switch v-model="newAdmin.adminManage" active-value="true" inactive-value="false"></el-switch>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="onSubmit" class="end">立即创建</el-button>
        <el-button>取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
export default {
  data() {
    return {
      newAdmin: {
        adminName: '',
        adminKey: '',
        courseManege: false,
        userManege: false,
        historyManage: false,
        orderManege: false,
        adminManage: false
      }
    }
  },
  methods: {
    onSubmit() {
    },
    // 当开关触发后对应绑定的value会变化（分别为true和false）
    // @change 为开关改变状态触发的参数，返回值是当前绑定的value
    newv: function(callback) {
    }
  }
}
</script>
<style scoped>
  .addAdmin {
    width: 400px;
    margin-left: 100px;
  }
</style>
