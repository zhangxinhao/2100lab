<template>
  <div>
    <div class="browstitle">
      <div class="browshead">已购课程</div>
      <div id="usertable">
      <el-table
        class="ordertable"
        :data="paidCourseList">
        <el-table-column
          header-align=center
          prop="course_id"
          label="课程编号"
          >
        </el-table-column>
        <el-table-column
          header-align=center
          prop="course_name"
          label="课程名字"
        >
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
          :current-page.sync="nowPage"
          :pager-count="5"
          small>
        </el-pagination>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      list: [],
      paidCourseList: [
        {course_id: '110', course_name: '1', money: '56', time: '2018-3-5'},
        {course_id: '110', course_name: '1', money: '44', time: '2018-3-5'},
        {course_id: '110', course_name: '1', money: '34', time: '2018-3-5'},
        {course_id: '110', course_name: '1', money: '45', time: '2018-3-5'},
        {course_id: '110', course_name: '1', money: '12', time: '2018-3-5'},
        {course_id: '110', course_name: '1', money: '24', time: '2018-3-5'}
      ],
      nowPage: 1,
      pageSize: 2,
      totalNumber: 10
    }
  },
  methods: {
  }
}
</script>
<style>
  .browstitle {
    width: 900px;
  }
  #usertable {
    margin-bottom: 50px;
  }
  .browshead {
    font-size: 20px;
    color: black;
    font-weight: bold;
    margin-bottom: 30px;
  }
  @media screen and (max-width: 500px) {
    .browstitle {
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
