<template>
  <div class="firstDiv">
    <div class="searchOrder">
      <el-input class="searchbox" v-model="input" placeholder="请输入查询课程编号"></el-input><el-button class="btn" type="primary" icon="el-icon-search">搜索</el-button>
    </div>
    <div class="orderTable">
      <div class="orderHead">用户浏览</div>
      <div class="reallyTable">
      <el-table
        border="true"
        :data="userBrowsList"
        style="width: 100%">
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
          prop="lastTime"
          label="浏览时间">
        </el-table-column>
      </el-table>
      </div>
      <div style="text-align: center">
        <el-pagination
          background
          layout="prev, pager, next"
          :total="userBrowsList.length"
          page-size="5"
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
      userBrowsList: [
        {courseId: '123', userId: '1', lastTime: '2018-3-6'},
        {courseId: '124', userId: '5', lastTime: '2018-8-4'},
        {courseId: '128', userId: '1', lastTime: '2018-5-12'},
        {courseId: '121', userId: '3', lastTime: '2018-5-23'},
        {courseId: '125', userId: '1', lastTime: '2018-3-6'},
        {courseId: '123', userId: '2', lastTime: '2018-3-6'},
        {courseId: '123', userId: '1', lastTime: '2018-3-6'}
      ]
    }
  }
}
</script>
<style>
  .searchOrder {
    width:300px;
    margin-left: 50px;
    margin-bottom: 60px;
  }
  .searchbox {
    width: 70%;
  }
  .btn {
    width: 30%;
  }
  .orderHead {
    font-size: 20px;
    color:black;
    font-weight: bold;
    margin-bottom: 30px;
  }
  .orderTable {
    margin-left: 50px;
    width: 700px;
    margin-bottom: 50px;
  }
  .reallyTable {
    margin-bottom: 50px;
  }
  .firstDiv {
    width: 1200px;
  }
</style>
