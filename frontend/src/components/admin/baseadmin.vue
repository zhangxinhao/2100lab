<template>
  <div clsss="outdiv">
    <el-container class="adminfirst">
      <el-header class="adminheader">Header</el-header>
      <el-container class="adminsecond">
        <el-aside class="adminaside">
          <el-menu @select="handleSelect" unique-opened:false >
            <el-submenu index="1">
              <template class="firsebar" slot="title"><i class="el-icon-edit"></i>课程管理</template>
              <el-menu-item class="col" index="1-1">课程上传</el-menu-item>
              <el-menu-item class="col" index="1-2">课程编辑</el-menu-item>
            </el-submenu>
            <el-submenu index="2">
              <template class="secondbar" slot="title"><i class="el-icon-document"></i>管理用户</template>
              <el-menu-item class="col" index="2-1">用户信息</el-menu-item>
              <el-menu-item class="col" index="2-2">用户浏览</el-menu-item>
              <el-menu-item class="col" index="2-3">留言管理</el-menu-item>
            </el-submenu>
            <el-submenu index="3">
              <template class="secondbar" slot="title"><i class="el-icon-date"></i>操作历史</template>
              <el-menu-item class="col" index="3-1">后台操作历史</el-menu-item>
            </el-submenu>
             <el-submenu index="4">
              <template class="secondbar" slot="title"><i class="el-icon-news"></i>订单管理</template>
              <el-menu-item class="col" index="4-1">用户订单</el-menu-item>
            </el-submenu>
             <el-submenu index="5">
              <template class="secondbar" slot="title"><i class="el-icon-view"></i>数据统计</template>
              <el-menu-item class="col" index="5-1">数据分析</el-menu-item>
            </el-submenu>
             <el-submenu index="6">
              <template class="secondbar" slot="title"><i class="el-icon-plus"></i>管理员操作</template>
              <el-menu-item class="col" index="6-1">新增管理员</el-menu-item>
              <el-menu-item class="col" index="6-2">编辑管理员</el-menu-item>
            </el-submenu>
          </el-menu>
        </el-aside>
        <el-main>
          <router-view></router-view>
        </el-main>
      </el-container>
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
    },
    handleSelect(key, keyPath) {
      switch (key) {
        case '1-1':
          this.$router.push('/uploadCourse')
          break
        case '1-2':
          this.$router.push('/courseManage')
          break
        case '2-1':
          this.$router.push('/usermanage')
          break
        case '2-2':
          this.$router.push('/userBrowsing')
          break
        case '2-3':
          this.$router.push('/commentadmin')
          break
        case '3-1':
          this.$router.push('/adminHistory')
          break
        case '4-1':
          this.$router.push('/orderAdmin')
          break
        case '5-1':
          this.$router.push('/dataAnalize')
          break
        case '6-1':
          this.$router.push('/addAdmin')
          break
        case '6-2':
          this.$router.push('/adminManage')
          break
      }
    }
  }
}
</script>
<style scoped>
  .adminfirst {
    width: 1600px;
    margin: 0px auto 0px auto;
    text-align: center;
    color:#d2dce6;
  }
  .el-submenu__title {
    height: 60px !important;
    line-height:60px !important;
    background-color: rgb(238, 243, 247);
    font-size: 18px;
    vertical-align: middle;
    font-weight: bold;
  }
  .col {
    height: 60px;
  }
</style>
