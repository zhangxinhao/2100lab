<template>
  <div id="person">
    <el-container>
      <el-aside>
        <el-menu default-active="1" class="el-menu-vertical-demo" @select="handleSelect">
            <template class="head" slot="title"><i class="el-icon-message"></i>个人中心</template>
            <el-menu-item class="col" index="1">浏览历史</el-menu-item>
            <el-menu-item class="col" index="2">订单列表</el-menu-item>
            <el-menu-item class="col" index="3">已购课程</el-menu-item>
            <el-menu-item class="col" index="4">个人信息</el-menu-item>
        </el-menu>
      </el-aside>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </div>
</template>
<script>
export default {
  data() {
    return {
    }
  },
  methods: {
    handleChange(value) {
      console.log(value)
    },
    handleSelect(key,keyPath) {
      switch(key) {
        case '1':
          this.$router.push('/brows');
          break;
      }
    }
  }
}
</script>
<style>
  .el-aside {
    width: 300px !important;
    margin-left: 40px;
  }
  .col {
    height: 100px !important;
    line-height:100px !important;
    font-size: 20px;
    background-color:#EBEEF5;
  }
  .el-submenu__title {
    height: 100px !important;
    line-height:100px !important;
    background-color: #E4E7ED;
    font-size: 20px;
    vertical-align:middle;
    font-weight: bold;
  }
</style>
