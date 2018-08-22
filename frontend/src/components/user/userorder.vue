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
          prop="order_id"
          label="订单编号"
          width="180">
        </el-table-column>
        <el-table-column
          header-align=center
          prop="course_id"
          label="课程编号"
          width="180">
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
        {order_id: '110', course_id: '1', status: '已支付', time: '2018-3-5'},
        {order_id: '110', course_id: '1', status: '已支付', time: '2018-3-5'},
        {order_id: '110', course_id: '1', status: '已支付', time: '2018-3-5'},
        {order_id: '110', course_id: '1', status: '已支付', time: '2018-3-5'},
        {order_id: '110', course_id: '1', status: '已支付', time: '2018-3-5'},
        {order_id: '110', course_id: '1', status: '已支付', time: '2018-3-5'}
      ],
      nowPage: 1,
      pageSize: 2,
      totalNumber: 100
    }
  },
  methods: {
    flipOver: function (page) {
      let _end = this.pageSize * page
      let end = this.totalNumber < _end ? this.totalNumber : _end
      this.userOrderList = []
      let start = _end - this.pageSize
      for (let i = start; i < end; i++) {
        this.userOrderList.push({
          'order_id': this.list[i].order_id,
          'course_id': this.list[i].course_id,
          'status': this.list[i].status,
          'time': new Date(this.list[i].time * 1000).toLocaleString().replace(/:\d{1,2}$/, ' ')
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
          'order_id': this.list[i].order_id,
          'course_id': this.list[i].course_id,
          'status': this.list[i].status,
          'time': new Date(this.list[i].time * 1000).toLocaleString().replace(/:\d{1,2}$/, ' ')
        })
      }
    })
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
