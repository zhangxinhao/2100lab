<template>
<div class="admin-history">

  <div id="search-history">
    <el-row :gutter="20">
      <el-col :span="6" :offset="7">
        <el-input v-model="searchAdminId" placeholder="请输入管理员编号">
        </el-input>
      </el-col>
      <el-col :span="6" :offset="1">
        <el-input v-model="searchObjectId" placeholder="请输入对象编号">
        </el-input>
      </el-col>
      <el-col :span="2">
        <el-button type="primary"
          icon="el-icon-search"
          @click="getList"
          class="search-btn">
          搜索
        </el-button>
      </el-col>
    </el-row>
  </div>

  <div id="history-list">
    <el-table :data="historyData" border width=100%>
      <el-table-column type="index"
        :index="indexMethod"
        header-align=center>
      </el-table-column>
      <el-table-column
        prop="adminId"
        label="管理员编号"
        width="150"
        header-align=center>
      </el-table-column>
      <el-table-column
        prop="operation"
        label="操作"
        width="150"
        header-align=center>
      </el-table-column>
      <el-table-column
        prop="objectId"
        label="对象编号"
        width="150"
        header-align=center>
      </el-table-column>
      <el-table-column
        prop="time"
        label="操作时间"
        header-align=center>
      </el-table-column>
    </el-table>
  </div>

</div>
</template>

<script>
import * as utils from '../utils/utils.js'
import axios from 'axios'
import qs from 'qs'

export default {
  data() {
    return {
      searchAdminId: '',
      searchObjectId: '',
      historyData: [
        {
          adminId: '001',
          operation: '添加课程',
          objectId: '15223',
          time: '2018.08.20'
        },
        {
          adminId: '002',
          operation: '删除用户',
          objectId: '15222681355',
          time: '2018.08.19'
        }
      ]
    }
  },
  methods: {
    indexMethod: function(index) {
      return index + 1
    },
    getList: function() {
      axios.post(utils.getURL() + 'api/recordlist/', qs.stringify({
        adminId: this.searchAdminId,
        objectId: this.searchObjectId
      })).then(response => {
        if (response.data.status === 0) {
          this.historyData = response.data.history
        } else {
          this.$message.error('内部错误')
        }
      })
    }
  },
  created: function() {
    this.getList()
  }
}
</script>

<style scoped>
  .admin-history {
    width: 80%;
    margin: 20px 5%;
  }
  #history-list {
    width: 100%;
    min-height: 1000px;
    margin: 50px auto;
    text-align: center;
  }
</style>
