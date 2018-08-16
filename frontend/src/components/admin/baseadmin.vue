<template>
  <div>
    <el-container class="adminFirst">
      <el-header class="adminHeader">Header</el-header>
      <el-container class="adminSecond">
        <el-aside class="adminAside">
          <el-menu @select="handleSelect" :default-openeds="['1', '6']">
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
              <template class="secondbar" slot="title"><i class="el-icon-view"></i>统计</template>
              <el-menu-item class="col" index="5-1">数据分析</el-menu-item>
            </el-submenu>
             <el-submenu index="6">
              <template class="secondbar" slot="title"><i class="el-icon-plus"></i>添加管理员</template>
              <el-menu-item class="col" index="6-1">新增管理员</el-menu-item>
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
      console.log(value)
    }
  }
}
</script>
<style>
</style>
