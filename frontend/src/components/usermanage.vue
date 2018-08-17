<template>
<div class="user-manage">

  <div id="search-user">
    <el-row :gutter="20">
      <el-col :span="6" :offset="3"><el-input v-model="search_userId" placeholder="请输入用户ID"></el-input></el-col>
      <el-col :span="2"><el-button type="primary" icon="el-icon-search">搜索</el-button></el-col>
      <el-col :span="6" :offset="2"><el-input v-model="search_userName" placeholder="请输入昵称"></el-input></el-col>
      <el-col :span="2"><el-button type="primary" icon="el-icon-search">搜索</el-button></el-col>
    </el-row>
  </div>

  <div id="user-list">
    <el-table :data="userData" border style="width: 100%">
      <el-table-column type="index" :index="indexMethod" header-align=center></el-table-column>
      <el-table-column prop="userId" label="用户ID" width="180" header-align=center></el-table-column>
      <el-table-column prop="userName" label="用户昵称" width="180" header-align=center></el-table-column>
      <el-table-column prop="balance" label="用户赏金" width="180" header-align=center></el-table-column>
      <el-table-column label="操作" header-align=center>
        <template slot-scope="scope">
          <el-button type="text" size="small" @click="editFunction(scope.$index)">删除用户</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>

  <div class="editDialog">
    <el-dialog title="删除用户" :visible.sync="editVisible" width="400px" height="700px">
      <div>确认要删除ID为：{{userData[editIndex].userId}} 的用户？</div>
      <div slot="footer" class="edit-footer">
        <el-button @click="editVisible = false">取 消</el-button>
        <el-button type="primary" @click="edit">确 定</el-button>
      </div>
    </el-dialog>
  </div>

</div>
</template>

<script>
export default {
  data() {
    return {
      search_userId: '',
      search_userName: '',
      index: 0,
      editIndex: 0,
      editVisible: false,
      userData: [
        {userId: '15222681355', userName: 'zzgyy', balance: 250},
        {userId: '15222681356', userName: 'gyysz', balance: 250}
      ]
    }
  },
  methods: {
    indexMethod(index) {
      return index + 1
    },
    editFunction(editIndex) {
      this.editVisible = true
      console.log(editIndex)
      this.editIndex = editIndex
    },
    edit() {
      this.editVisible = false
    }
  }
}
</script>

<style scoped>
.user-manage {
  width: 1020px;
  margin: 20px auto;
}
#search-user {
  width: 1000px;
}
#user-list {
  width: 800px;
  height: 1000px;
  margin: 50px auto;
  text-align: center;
}
</style>
