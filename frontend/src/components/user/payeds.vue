<template>
  <div>
    <div class="brows-title">
      <div class="brows-head">已购课程</div>
      <div id="user-table">
        <el-table
          :data="paidCourseList">
          <el-table-column
            header-align=center
            prop="courseId"
            label="课程编号">
          </el-table-column>
          <el-table-column
            header-align=center
            prop="courseName"
            label="课程名字">
          </el-table-column>
          <el-table-column
            header-align=center
            prop="money"
            label="课程金额">
          </el-table-column>
          <el-table-column
            header-align=center
            prop="time"
            label="购买时间">
          </el-table-column>
        </el-table>
      </div>

      <div>
        <el-pagination
          background
          layout="prev, pager, next"
          :total="totalNumber"
          :page-size="pageSize"
          :current-page.sync="pageNo"
          :pager-count="5"
          @current-change="flipeOver"
          small>
        </el-pagination>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import * as utils from '../utils/utils.js'

export default {
  data() {
    return {
      list: [],
      paidCourseList: [
        {courseId: '110', courseName: '1', money: '56', time: '2018-3-5'},
        {courseId: '110', courseName: '1', money: '44', time: '2018-3-5'},
        {courseId: '110', courseName: '1', money: '34', time: '2018-3-5'},
        {courseId: '110', courseName: '1', money: '45', time: '2018-3-5'},
        {courseId: '110', courseName: '1', money: '12', time: '2018-3-5'},
        {courseId: '110', courseName: '1', money: '24', time: '2018-3-5'}
      ],
      pageNo: 1,
      pageSize: 2,
      totalNumber: 10
    }
  },
  methods: {
    flipeOver: function (page) {
      let totalEnd = this.pageSize * page
      let end = this.totalNumber < (totalEnd) ? this.totalNumber : totalEnd
      this.paidCourseList = []
      let start = this.pageSize * (page - 1)
      for (let i = start; i < end; i++) {
        this.paidCourseList.push(this.list[i])
      }
    }
  },
  created: function() {
    axios.post(utils.getURL() + 'api/listorders/').then(response => {
      let lists = response.data.orders
      this.list = []
      for (let i = 0; i < response.data.orders.length; i++) {
        this.list.push({
          'courseId': lists[i].course_id,
          'courseName': lists[i].course_name,
          'money': lists[i].price,
          'time': lists[i].time
        })
      }
      this.totalNumber = this.list.length
      let totalNumber = this.totalNumber
      this.paidCourseList = []
      let size = this.pageSize
      if (totalNumber < size) {
        this.paidCourseList = this.list
      } else {
        for (let i = 0; i < size; i++) {
          this.paidCourseList.push(this.list[i])
        }
      }
    })
  }
}
</script>
<style>
  .brows-title {
    width: 900px;
  }
  #user-table {
    margin-bottom: 50px;
  }
  .brows-head {
    font-size: 20px;
    color: black;
    font-weight: bold;
    margin-bottom: 30px;
  }

  @media screen and (max-width: 500px) {
    .brows-title {
      width: 260px;
    }
    .el-table__header {
      width: 260px !important;
    }
    .el-table__body {
      width: 260px !important;
    }
    col {
      width: 50px !important;
    }
    .el-table {
      font-size: 7px;
    }
}
</style>
