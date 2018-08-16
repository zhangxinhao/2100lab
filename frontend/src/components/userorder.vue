<template>
  <div>
    <div class="browsTitle">
      <div class="browsHead">浏览历史</div>
      <hr />
      <div>
      <el-table
        :data="userOrderList"
        style="width: 100%">
        <el-table-column
          prop="userOrderId"
          label="订单编号"
          width="180">
        </el-table-column>
        <el-table-column
          prop="courseId"
          label="课程编号"
          width="180">
        </el-table-column>
        <el-table-column
          prop="orderStatus"
          label="是否支付">
        </el-table-column>
        <el-table-column
          prop="orderTime"
          label="时间">
        </el-table-column>
      </el-table>
    </div>
    </div>

    <div style="text-align: center">
        <el-pagination
          background
          layout="prev, pager, next"
          :total="userOrderList.length"
          page-size="5"
          :current-page.sync="nowPage"
          :pager-count="5"
          >
        </el-pagination>
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
    handleChange(value) {
      console.log(value)
    }
  }
}
</script>
<style>
</style>
