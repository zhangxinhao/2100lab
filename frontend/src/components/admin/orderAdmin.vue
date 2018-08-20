<template>
  <div class="firstDiv">
    <div class="searchOrder">
      <el-input class="searchbox" v-model="inputword" placeholder="请输入查询订单号"></el-input><el-button class="btn" type="primary" icon="el-icon-search" @click="search">搜索</el-button>
    </div>
    <div class="orderTable">
      <div class="orderHead">订单列表</div>
      <div class="reallyTable">
      <el-table
        border
        :data="userOrderList"
        style="width: 100%">
        <el-table-column
          header-align=center
          prop="userOrderId"
          label="订单编号"
          width="150">
        </el-table-column>
         <el-table-column
          header-align=center
          prop="userId"
          label="用户账号"
          width="150">
        </el-table-column>
        <el-table-column
          header-align=center
          prop="courseId"
          label="课程编号"
          width="150">
        </el-table-column>
        <el-table-column
          header-align=center
          prop="orderStatus"
          label="是否支付"
          width="150">
        </el-table-column>
        <el-table-column
          header-align=center
          prop="orderTime"
          label="交易时间"
          width="250">
        </el-table-column>
        <el-table-column
          header-align=center
          label="操作">
          <template slot-scope="scope">
            <el-button  type="text">退费</el-button>
          </template>
        </el-table-column>
      </el-table>
      </div>
      <div style="text-align: center">
        <el-pagination
          background
          layout="prev, pager, next"
          :total="userOrderList.length"
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
      userOrderList: [
        {userOrderId: '110', userId: '12', courseId: '1', orderStatus: '已支付', orderTime: '2018-3-5'},
        {userOrderId: '110', userId: '12', courseId: '1', orderStatus: '已退费', orderTime: '2018-3-5'},
        {userOrderId: '110', userId: '12', courseId: '1', orderStatus: '已支付', orderTime: '2018-3-5'},
        {userOrderId: '110', userId: '12', courseId: '1', orderStatus: '未支付', orderTime: '2018-3-5'},
        {userOrderId: '110', userId: '12', courseId: '1', orderStatus: '已支付', orderTime: '2018-3-5'},
        {userOrderId: '110', userId: '12', courseId: '1', orderStatus: '已支付', orderTime: '2018-3-5'}
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
    width: 950px;
    margin-bottom: 50px;
  }
  .reallyTable {
    margin-bottom: 50px;
  }
  .firstDiv {
    width: 1200px;
    margin: 50px auto;
    text-align: center;
  }
</style>
