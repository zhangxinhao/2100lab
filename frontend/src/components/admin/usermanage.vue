<template>
<div class="user-manage">

  <div id="search-user">
    <el-row :gutter="20">
      <el-col :span="6" :offset="8"><el-input v-model="search_userId" placeholder="请输入用户ID"></el-input></el-col>
      <el-col :span="6" :offset="1"><el-input v-model="search_userAlias" placeholder="请输入昵称"></el-input></el-col>
      <el-col :span="2"><el-button type="primary" icon="el-icon-search">搜索</el-button></el-col>
    </el-row>
  </div>

  <div id="user-list">
    <el-table :data="userData" border width=100%>
      <el-table-column type="index" :index="indexMethod" header-align=center></el-table-column>
      <el-table-column prop="userId" label="用户ID" width="250" header-align=center></el-table-column>
      <el-table-column prop="userAlias" label="用户昵称" width="220" header-align=center></el-table-column>
      <el-table-column prop="bonus" label="用户赏金" width="220" header-align=center></el-table-column>
      <el-table-column label="操作" header-align=center>
        <template slot-scope="scope">
          <el-button type="text" size="small" @click="deleteFunction(scope.$index)">删除用户</el-button>
          <el-button type="text" size="small" @click="forbideFunction(scope.$index)">禁言用户</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>

  <div style="text-align:right">
    <el-pagination
      background
      layout="prev, pager, next"
      :page-size="pageSize"
      :total="totalnumber"
      :current-page.sync="pageNo"
      :pager-count="7"
      @current-change="flipeOver"
      >
    </el-pagination>
  </div>

  <div class="deletedialog">
    <el-dialog title="删除用户" :visible.sync="deleteVisible" width="400px" height="700px">
      <div>确认要删除ID为：{{userData[deleteIndex].userId}} 的用户？</div>
      <div slot="footer" class="delete-footer">
        <el-button @click="deleteVisible = false">取 消</el-button>
        <el-button type="primary" @click="deleteuser">确 定</el-button>
      </div>
    </el-dialog>
  </div>
  <div class="forbidedialog">
    <el-dialog title="删除用户" :visible.sync="forbideVisible" width="400px" height="700px">
      <div>确认要禁言ID为：{{userData[forbideIndex].userId}} 的用户？</div>
      <div slot="footer" class="forbide-footer">
        <el-button @click="forbideVisible = false">取 消</el-button>
        <el-button type="primary" @click="forbideuser">确 定</el-button>
      </div>
    </el-dialog>
  </div>

</div>
</template>

<script>
import axios from 'axios'
// import qs from 'qs'

export default {
  data() {
    return {
      search_userId: '',
      search_userAlias: '',
      index: 0,
      deleteIndex: 0,
      deleteVisible: false,
      forbideIndex: 0,
      forbideVisible: false,
      list: [],
      userData: [
        {userId: '15222681355', userAlias: 'zzgyy', bonus: 250},
        {userId: '15222681356', userAlias: 'gyysz', bonus: 250}
      ],
      pageSize: 20,
      totalnumber: 100,
      pageNo: 1
    }
  },
  methods: {
    indexMethod(index) {
      return index + 1
    },
    deleteFunction(deleteIndex) {
      this.deleteVisible = true
      this.deleteIndex = deleteIndex
    },
    deleteuser() {
      this.deleteVisible = false
    },
    forbideFunction(forbideIndex) {
      this.forbideVisible = true
      this.forbideIndex = forbideIndex
    },
    forbideuser() {
      this.forbideVisible = false
    },
    flipOver(page) {
      let _end = this.pageSize * page
      let end = this.totalnumber < _end ? this.totalnumber : _end
      this.userData = []
      let start = this.pageSize * (page - 1)
      for (let i = start; i < end; i++) {
        this.userData.push(this.list[i])
      }
    }
  },
  created: function() {
    axios.post('http://192.168.55.33:8000/api/clientinfor/').then(response => {
      this.list = response.data.query
      this.totalnumber = this.list.length
      let totalnumber = this.totalnumber
      this.userData = []
      let size = this.pageSize
      if (totalnumber < size) {
        this.userData = this.list
      } else {
        for (let i = 0; i < size; i++) {
          this.userData.push(this.list[i])
        }
      }
    })
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
  width: 1000px;
  height: 1000px;
  margin: 50px auto;
  text-align: center;
}
</style>
