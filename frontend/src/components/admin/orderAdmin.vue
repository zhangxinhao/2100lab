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
          prop="orderNo"
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
          prop="status"
          label="订单状态"
          width="150">
        </el-table-column>
        <el-table-column
          header-align=center
          prop="time"
          label="交易时间"
          width="250">
        </el-table-column>
        <el-table-column
          header-align=center
          label="操作">
          <template slot-scope="scope">
            <el-button  type="text" v-if="userOrderList[scope.$index].status == '已支付'">退费</el-button>
            <el-button  type="text" v-else>&mdash;</el-button>

          </template>
        </el-table-column>
      </el-table>
      </div>
      <div style="text-align: center">
        <el-pagination
          background
          layout="prev, pager, next"
          :page-size="pageSize"
          :total="totalnumber"
          :current-page.sync="pageNo"
          :pager-count="7"
          @current-change="flipOver"
          >
        </el-pagination>
      </div>
    </div>
  </div>
</template>

<script>
import * as utils from '../utils/utils.js'
import axios from 'axios'
import qs from 'qs'

export default {
  data() {
    return {
      inputword: '',
      list: [],
      userOrderList: [
        {orderNo: '110', userId: '12', courseId: '1', status: '已支付', time: '2018-3-5'},
        {orderNo: '110', userId: '12', courseId: '1', status: '已退费', time: '2018-3-5'},
        {orderNo: '110', userId: '12', courseId: '1', status: '已支付', time: '2018-3-5'},
        {orderNo: '110', userId: '12', courseId: '1', status: '未支付', time: '2018-3-5'},
        {orderNo: '110', userId: '12', courseId: '1', status: '已支付', time: '2018-3-5'},
        {orderNo: '110', userId: '12', courseId: '1', status: '已支付', time: '2018-3-5'}
      ],
      pageSize: 12,
      totalnumber: 100,
      pageNo: 1
    }
  },
  methods: {
    search: function() {
      axios.post(utils.getURL() + 'api/manageorder/', qs.stringify({
        orderNo: this.inputword
      })).then(response => {
        if (response.data.status === 0) {
          this.userOrderList = response.data.orders
        } else {
          alert('订单号错误')
          this.userOrderList = []
        }
      })
    },
    flipOver: function(page) {
      let _end = this.pageSize * page
      let end = this.totalnumber < (_end) ? this.totalnumber : _end
      this.userOrderList = []
      let start = this.pageSize * (page - 1)
      for (let i = start; i < end; i++) {
        this.userOrderList.push(this.list[i])
      }
    }
  },
  created: function() {
    axios.post(utils.getURL() + 'api/manageorder/').then(response => {
      if (response.data.status === 0) {
        this.list = response.data.orders
        this.totalnumber = this.list.length
        let totalnumber = this.totalnumber
        this.userOrderList = []
        let size = this.pageSize
        if (totalnumber < size) {
          this.userOrderList = this.list
        } else {
          for (let i = 0; i < size; i++) {
            this.userOrderList.push(this.list[i])
          }
        }
      }
    })
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
