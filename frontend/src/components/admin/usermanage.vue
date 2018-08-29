<template>
<div class="user-manage">

  <div id="search-user">
    <el-row :gutter="20">
      <el-col :span="6" :offset="8">
        <el-input v-model="searchUserId" placeholder="请输入用户ID">
        </el-input>
      </el-col>
      <el-col :span="6" :offset="1">
        <el-input v-model="searchUserAlias" placeholder="请输入昵称">
        </el-input>
      </el-col>
      <el-col :span="2">
        <el-button type="primary" icon="el-icon-search" @click="search">
          搜索
        </el-button>
      </el-col>
    </el-row>
  </div>

  <div id="user-list">
    <el-table :data="userData" border width=100%>
      <el-table-column
        type="index"
        :index="indexMethod"
        header-align=center>
      </el-table-column>
      <el-table-column
        prop="userId"
        label="用户ID"
        width="180px"
        header-align=center>
      </el-table-column>
      <el-table-column
        prop="userAlias"
        label="用户昵称"
        width="180px"
        header-align=center>
      </el-table-column>
      <el-table-column
        prop="isV"
        label="用户认证"
        width="100px"
        header-align=center
        :formatter="vCall">
      </el-table-column>
      <el-table-column
        prop="bonus"
        label="用户赏金"
        width="220px"
        header-align=center>
      </el-table-column>
      <el-table-column label="操作" header-align=center>
        <template slot-scope="scope">
          <el-button
            type="text"
            size="small"
            @click="deleteFunction(scope.$index)">
            删除
          </el-button>
          <el-button
            type="text"
            size="small"
            @click="forbideFunction(scope.$index)">
            禁言
          </el-button>
          <el-button
            type="text"
            size="small"
            @click="authorizeFunction(scope.$index)">
            认证
          </el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>

  <div class="pager">
    <el-pagination
      background
      layout="prev, pager, next"
      :page-size="pageSize"
      :total="totalNumber"
      :current-page.sync="pageNo"
      :pager-count="7"
      @current-change="flipOver"
      >
    </el-pagination>
  </div>

  <div class="delete-dialog">
    <el-dialog
      title="删除用户"
      :visible.sync="deleteVisible"
      width="400px"
      height="700px">
      <div>
        确认要删除ID为：{{ index }} 的用户?
      </div>
      <div slot="footer" class="delete-footer">
        <el-button @click="deleteVisible = false">取 消</el-button>
        <el-button type="primary" @click="deleteUser">确 定</el-button>
      </div>
    </el-dialog>
  </div>
  <div class="forbide-dialog">
    <el-dialog title="禁言用户"
      :visible.sync="forbideVisible"
      width="400px"
      height="700px">
      <div>
        确认要禁言ID为：{{ index }} 的用户?
      </div>
      <div slot="footer" class="forbide-footer">
        <el-button @click="forbideVisible = false">取 消</el-button>
        <el-button type="primary" @click="forbideUser">确 定</el-button>
      </div>
    </el-dialog>
  </div>

</div>
</template>

<script>
import axios from 'axios'
import qs from 'qs'
import * as utils from '../utils/utils.js'

export default {
  data() {
    return {
      searchUserId: '',
      searchUserAlias: '',
      index: 0,
      deleteIndex: 0,
      deleteVisible: false,
      forbideIndex: 0,
      forbideVisible: false,
      list: [],
      userData: [
        {
          userId: '15222681355',
          userAlias: 'zzgyy',
          isV: false,
          bonus: 250
        },
        {
          userId: '15222681356',
          userAlias: 'gyysz',
          isV: true,
          bonus: 250
        }
      ],
      pageSize: 20,
      totalNumber: 100,
      pageNo: 1
    }
  },
  methods: {
    vCall: function(data) {
      return data.isV ? '是' : '否'
    },
    indexMethod: function(index) {
      return index + 1
    },
    deleteFunction: function(deleteIndex) {
      this.deleteVisible = true
      this.index = this.userData[deleteIndex].userId
    },
    deleteUser: function() {
      axios.post(utils.getURL() + 'api/deleteclient/', qs.stringify({
        user_id: this.userData[this.deleteIndex].userId
      })).then(response => {
      })
      this.deleteVisible = false
    },
    forbideFunction: function(forbideIndex) {
      this.forbideVisible = true
      this.index = this.userData[forbideIndex].userId
    },
    forbideUser: function() {
      axios.post(utils.getURL() + 'api/banclient/', qs.stringify({
        user_id: this.userData[this.forbideIndex].userId
      })).then(response => {
      })
      this.forbideVisible = false
    },
    authorizeFunction: function(authorizeIndex) {
      axios.post(utils.getURL() + 'api/authorize/', qs.stringify({
        user_id: this.userData[authorizeIndex].userId,
        auth: !this.userData[authorizeIndex].isV
      })).then(response => {
        if (response.data.status === 0) {
          this.userData[authorizeIndex].isV =
            !this.userData[authorizeIndex].isV
          if (this.userData[authorizeIndex].isV) {
            this.$message({
              message: '认证成功！',
              type: 'success'
            })
          } else {
            this.$message({
              message: '取消认证成功！',
              type: 'success'
            })
          }
        }
      })
    },
    search: function() {
      axios.post(utils.getURL() + 'api/clientinfor/', qs.stringify({
        user_id: this.searchUserId,
        user_alias: this.searchUserAlias
      })).then(response => {
        this.list = response.data.query
        this.totalNumber = this.list.length
        let totalNumber = this.totalNumber
        this.userData = []
        let size = this.pageSize
        if (totalNumber < size) {
          this.userData = this.list
        } else {
          for (let i = 0; i < size; i++) {
            this.userData.push(this.list[i])
          }
        }
      })
    },
    flipOver: function(page) {
      let _end = this.pageSize * page
      let end = this.totalNumber < _end ? this.totalNumber : _end
      this.userData = []
      let start = this.pageSize * (page - 1)
      for (let i = start; i < end; i++) {
        this.userData.push(this.list[i])
      }
    }
  },
  created: function() {
    axios.post(utils.getURL() + 'api/clientinfor/').then(response => {
      this.list = response.data.query
      this.totalNumber = this.list.length
      let totalNumber = this.totalNumber
      this.userData = []
      let size = this.pageSize
      if (totalNumber < size) {
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
    width: 80%;
    margin: 20px auto;
  }
  #search-user {
    width: 100%;
  }
  #user-list {
    width: 100%;
    min-height: 1000px;
    margin: 50px auto;
    text-align: center;
  }
  .pager {
    text-align: right;
  }
</style>
