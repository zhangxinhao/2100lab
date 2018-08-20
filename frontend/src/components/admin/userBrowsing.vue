<template>
  <div class="firstdiv">
    <div class="searchorder">
      <el-input class="searchbox" v-model="inputword" placeholder="请输入查询课程编号"></el-input><el-button class="btn" type="primary" icon="el-icon-search" @click="search">搜索</el-button>
    </div>
    <div class="ordertable">
      <div class="orderhead">用户浏览</div>
      <div class="reallytable">
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
          :total="userBrowsList.length"
          :page-size="pageSize"
          :current-page.sync="nowPage"
          :pager-count="5">
        </el-pagination>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      inputword: '',
      userBrowsList: [
        {courseId: '123', userId: '1', userName: '丁一峰', lastTime: '2018-3-6'},
        {courseId: '124', userId: '5', userName: '丁一峰', lastTime: '2018-8-4'},
        {courseId: '128', userId: '1', userName: '丁一峰', lastTime: '2018-5-12'},
        {courseId: '121', userId: '3', userName: '丁一峰', lastTime: '2018-5-23'},
        {courseId: '125', userId: '1', userName: '丁一峰', lastTime: '2018-3-6'},
        {courseId: '123', userId: '2', userName: '丁一峰', lastTime: '2018-3-6'},
        {courseId: '123', userId: '1', userName: '丁一峰', lastTime: '2018-3-6'}
      ],
      nowPage: 1,
      pageSize: 2
    }
  },
  methods: {
    search: function() {
    }
  }
}
</script>
<style scoped>
  .searchorder {
    width: 300px;
    margin-left: 50px;
    margin-bottom: 60px;
  }
  .searchbox {
    width: 70%;
  }
  .btn {
    width: 30%;
  }
  .orderhead {
    font-size: 20px;
    color: black;
    font-weight: bold;
    margin-bottom: 30px;
  }
  .ordertable {
    margin-left: 50px;
    width: 1000px;
    margin-bottom: 50px;
  }
  .reallytable {
    margin-bottom: 50px;
  }
  .firstdiv {
    width: 1200px;
    margin: 50px auto;
    text-align: center;
  }
  .mytable {
    width: 100%
  }
</style>
