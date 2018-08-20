<template>
<div class="admin-history">

  <div id="search-history">
    <el-row :gutter="20">
      <el-col :span="6" :offset="3"><el-input v-model="search_adminId" placeholder="请输入管理员编号"></el-input></el-col>
      <el-col :span="2"><el-button type="primary" icon="el-icon-search">搜索</el-button></el-col>
      <el-col :span="6" :offset="2"><el-input v-model="search_objectId" placeholder="请输入对象编号"></el-input></el-col>
      <el-col :span="2"><el-button type="primary" icon="el-icon-search">搜索</el-button></el-col>
    </el-row>
  </div>

  <div id="history-list">
    <el-table :data="historyData" border width=100%>
      <el-table-column type="index" :index="indexMethod" header-align=center></el-table-column>
      <el-table-column prop="adminId" label="管理员编号" width="150" header-align=center></el-table-column>
      <el-table-column prop="operator" label="操作" width="150" header-align=center></el-table-column>
      <el-table-column prop="objectName" label="操作对象" width="150" header-align=center></el-table-column>
      <el-table-column prop="objectId" label="对象编号" width="150" header-align=center></el-table-column>
      <el-table-column prop="historyTime" label="操作时间" header-align=center></el-table-column>
    </el-table>
  </div>

</div>
</template>

<script>
export default {
  data() {
    return {
      search_adminId: '',
      search_objectId: '',
      historyData: [
        {adminId: '001', operator: '添加课程', objectName: '我们爱学习', objectId: '15223', historyTime: '2018.08.20'},
        {adminId: '002', operator: '删除用户', objectName: 'zzgyy', objectId: '15222681355', historyTime: '2018.08.19'}
      ]
    }
  },
  methods: {
    indexMethod(index) {
      return index + 1
    }
  }
}
</script>

<style scoped>
.admin-history {
  width: 1000px;
  margin: 20px auto;
}
#search-user {
  width: 900px;
}
#history-list {
  width: 900px;
  height: 1000px;
  margin: 50px auto;
  text-align: center;
}
</style>
