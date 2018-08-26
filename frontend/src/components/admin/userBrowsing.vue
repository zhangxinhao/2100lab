<template>
  <div class="first-div">
    <div class="search-order">
      <el-row>
        <el-col :span="18">
          <el-input class="search-box" v-model="input" placeholder="请输入查询课程编号"></el-input>
        </el-col>
        <el-col :span="6">
          <el-button class="btn" type="primary" icon="el-icon-search" @click="search(input)">搜索</el-button>
        </el-col>
      </el-row>
    </div>
    <div class="order-table">
      <div class="order-head">用户浏览</div>
      <div class="really-table">
      <el-table
        border
        class="mytable"
        :data="userBrowsList">
        <el-table-column
          header-align=center
          prop="courseId"
          label="课程编号"
          width="200">
        </el-table-column>
         <el-table-column
          header-align=center
          prop="userId"
          label="用户账号"
          width="200">
        </el-table-column>
        <el-table-column
          header-align=center
          prop="userName"
          label="用户昵称"
          width="300">
        </el-table-column>
        <el-table-column
          header-align=center
          prop="lastTime"
          label="浏览时间">
        </el-table-column>
      </el-table>
      </div>
      <div>
        <el-pagination
          background
          layout="prev, pager, next"
          :total="totalNumber"
          :page-size="pageSize"
          :current-page.sync="nowPage"
          :pager-count="5"
          @current-change="flipOver"
          >
        </el-pagination>
      </div>
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
      input: '',
      list: [],
      userBrowsList: [
        {courseId: '123', userId: '1', userName: 'dyf', lastTime: '2018-3-6'},
        {courseId: '124', userId: '5', userName: 'dyf', lastTime: '2018-8-4'},
        {courseId: '128', userId: '1', userName: 'dyf', lastTime: '2018-5-12'},
        {courseId: '121', userId: '3', userName: 'dyf', lastTime: '2018-5-23'},
        {courseId: '125', userId: '1', userName: 'dyf', lastTime: '2018-3-6'},
        {courseId: '123', userId: '2', userName: 'dyf', lastTime: '2018-3-6'},
        {courseId: '123', userId: '1', userName: 'dyf', lastTime: '2018-3-6'}
      ],
      nowPage: 1,
      pageSize: 10,
      totalNumber: 10
    }
  },
  methods: {
    flipOver: function(page) {
      let _end = this.pageSize * page
      let end = this.totalNumber < _end ? this.totalNumber : _end
      this.userBrowsList = []
      let start = _end - this.pageSize
      for (let i = start; i < end; i++) {
        this.userBrowsList.push({
          courseId: this.list[i].course_id,
          userId: this.list[i].user_id,
          userName: this.list[i].alias,
          lastTime: new Date(this.list[i].last_visit * 1000).toLocaleString().replace(/:\d{1,2}$/, ' ')
        })
      }
    },
    search: function(id) {
      axios.post(utils.getURL() + 'api/admin_userhistory/', qs.stringify({
        course_id: id
      })).then(response => {
        this.userBrowsList = []
        this.list = response.data.history
        this.totalNumber = this.list.length
        let end
        if (this.pageSize > this.totalNumber) {
          end = this.totalNumber
        } else {
          end = this.pageSize
        }
        for (let i = 0; i < end; i++) {
          this.userBrowsList.push({
            courseId: this.list[i].course_id,
            userId: this.list[i].user_id,
            userName: this.list[i].alias,
            lastTime: new Date(this.list[i].last_visit * 1000).toLocaleString().replace(/:\d{1,2}$/, ' ')
          })
        }
      })
    }
  },
  created: function() {
    axios.post(utils.getURL() + 'api/admin_userhistory/').then(response => {
      this.list = response.data.history
      this.totalNumber = this.list.length
      this.userBrowsList = []
      let end
      if (this.pageSize > this.totalNumber) {
        end = this.totalNumber
      } else {
        end = this.pageSize
      }
      for (let i = 0; i < end; i++) {
        this.userBrowsList.push({
          courseId: this.list[i].course_id,
          userId: this.list[i].user_id,
          userName: this.list[i].alias,
          lastTime: new Date(this.list[i].last_visit * 1000).toLocaleString().replace(/:\d{1,2}$/, ' ')
        })
      }
    })
  }
}
</script>
<style scoped>
  .search-order {
    width: 300px;
    margin-left: 50px;
    margin-bottom: 60px;
  }
  .search-box {
    width: 70%;
  }
  .order-head {
    font-size: 20px;
    color: black;
    font-weight: bold;
    margin-bottom: 30px;
  }
  .order-table {
    margin-left: 50px;
    width: 1000px;
    margin-bottom: 50px;
  }
  .really-table {
    margin-bottom: 50px;
  }
  .first-div {
    width: 1200px;
    margin: 50px auto;
    text-align: center;
  }
  .mytable {
    width: 100%
  }
</style>
