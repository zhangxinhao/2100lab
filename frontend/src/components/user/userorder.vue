<template>
  <div>
    <div class="brow-stitle">
      <div class="brows-head">订单列表</div>
      <div id="user-table">
        <el-table
          class="order-table"
          :data="userOrderList">
          <el-table-column
            header-align=center
            prop="orderId"
            label="订单编号">
          </el-table-column>
          <el-table-column
            header-align=center
            prop="courseId"
            label="课程编号">
          </el-table-column>
          <el-table-column
            header-align=center
            prop="status"
            label="是否支付">
          </el-table-column>
          <el-table-column
            header-align=center
            prop="time"
            label="时间">
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
          small
          @current-change="flipOver">
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
      userOrderList: [
        {orderId: '110', courseId: '1', status: '已支付', time: '2018-3-5'},
        {orderId: '110', courseId: '1', status: '已支付', time: '2018-3-5'},
        {orderId: '110', courseId: '1', status: '已支付', time: '2018-3-5'},
        {orderId: '110', courseId: '1', status: '已支付', time: '2018-3-5'},
        {orderId: '110', courseId: '1', status: '已支付', time: '2018-3-5'},
        {orderId: '110', courseId: '1', status: '已支付', time: '2018-3-5'}
      ],
      nowPage: 1,
      pageSize: 2,
      totalNumber: 10
    }
  },
  methods: {
    flipOver: function (page) {
      let totalEnd = this.pageSize * page
      let end = this.totalNumber < totalEnd ? this.totalNumber : totalEnd
      this.userOrderList = []
      let start = totalEnd - this.pageSize
      for (let i = start; i < end; i++) {
        this.userOrderList.push({
          'order_id': this.list[i].orderId,
          'course_id': this.list[i].courseId,
          'status': this.list[i].status,
          'time': new Date(this.list[i].time * 1000)
            .toLocaleString().replace(/:\d{1,2}$/, ' ')
        })
      }
    }
  },
  beforeCreate: function() {
    axios.post(utils.getURL() + 'api/listorders/').then(response => {
      this.userOrderList = []
      this.list = response.data.orders
      this.totalNumber = this.list.length
      let size = this.pageSize
      let end
      if (this.totalNumber < size) {
        end = this.totalNumber
      } else {
        end = size
      }
      for (let i = 0; i < end; i++) {
        this.userOrderList.push({
          'order_id': this.list[i].orderId,
          'course_id': this.list[i].courseId,
          'status': this.list[i].status,
          'time': new Date(this.list[i].time * 1000)
            .toLocaleString().replace(/:\d{1,2}$/, ' ')
        })
      }
    })
  }
}
</script>
<style>
  .brow-stitle {
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
    .brow-stitle {
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
