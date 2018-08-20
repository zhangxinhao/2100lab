<template>
  <div>
    <div class="browstitle">
      <div class="browshead">订单列表</div>
      <div id="usertable">
      <el-table
        border
        class="ordertable"
        :data="userOrderList">
        <el-table-column
          header-align=center
          prop="userOrderId"
          label="订单编号"
          width="180">
        </el-table-column>
        <el-table-column
          header-align=center
          prop="courseId"
          label="课程编号"
          width="180">
        </el-table-column>
        <el-table-column
          header-align=center
          prop="orderStatus"
          label="是否支付">
        </el-table-column>
        <el-table-column
          header-align=center
          prop="orderTime"
          label="时间">
        </el-table-column>
      </el-table>
      </div>

      <div>
        <el-pagination
          background
          layout="prev, pager, next"
          :total="userOrderList.length"
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
      userOrderList: [
        {userOrderId: '110', courseId: '1', orderStatus: '已支付', orderTime: '2018-3-5'},
        {userOrderId: '110', courseId: '1', orderStatus: '已支付', orderTime: '2018-3-5'},
        {userOrderId: '110', courseId: '1', orderStatus: '已支付', orderTime: '2018-3-5'},
        {userOrderId: '110', courseId: '1', orderStatus: '已支付', orderTime: '2018-3-5'},
        {userOrderId: '110', courseId: '1', orderStatus: '已支付', orderTime: '2018-3-5'},
        {userOrderId: '110', courseId: '1', orderStatus: '已支付', orderTime: '2018-3-5'}
      ],
      nowPage: 1
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
</style>
