<template>
  <div class="first-div">
    <div class="search-order">
      <el-row>
        <el-col :span="18">
          <el-input
            class="search-box"
            v-model="inputWord"
            placeholder="请输入查询订单号">
          </el-input>
        </el-col>
        <el-col :span="6">
          <el-button class="btn"
            type="primary"
            icon="el-icon-search"
            @click="search">
            搜索
          </el-button>
        </el-col>
      </el-row>
    </div>
    <div class="order-table">
      <div class="order-head">订单列表</div>
      <div class="really-table">
      <el-table
        border
        :data="userOrderList"
        class="list-table">
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
          width="100">
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
            <el-button  type="text"
              v-if="userOrderList[scope.$index].status == '已支付'"
              @click="refund(scope.$index)">
              退费
            </el-button>
            <el-button type="text" v-else>—</el-button>
          </template>
        </el-table-column>
      </el-table>
      </div>
      <div class="pager">
        <el-pagination
          background
          layout="prev, pager, next"
          :page-size="pageSize"
          :total="totalNumber"
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
      inputWord: '',
      list: [],
      userOrderList: [
        {
          orderNo: '110',
          userId: '12',
          courseId: '1',
          status: '已支付',
          time: '2018-3-5'
        },
        {
          orderNo: '110',
          userId: '12',
          courseId: '1',
          status: '已退费',
          time: '2018-3-5'
        },
        {
          orderNo: '110',
          userId: '12',
          courseId: '1',
          status: '已支付',
          time: '2018-3-5'
        },
        {
          orderNo: '110',
          userId: '12',
          courseId: '1',
          status: '未支付',
          time: '2018-3-5'
        },
        {
          orderNo: '110',
          userId: '12',
          courseId: '1',
          status: '已支付',
          time: '2018-3-5'
        },
        {
          orderNo: '110',
          userId: '12',
          courseId: '1',
          status: '已支付',
          time: '2018-3-5'
        }
      ],
      pageSize: 12,
      totalNumber: 100,
      pageNo: 1
    }
  },
  methods: {
    refund: function(index) {
      let orderNo = this.userOrderList[index].orderNo
      axios.post(utils.getURL() + 'api/refund/', qs.stringify({
        orderNo: orderNo
      })).then(response => {
        this.$message(response.data.result)
      })
    },
    search: function() {
      axios.post(utils.getURL() + 'api/manageorder/', qs.stringify({
        orderNo: this.inputWord
      })).then(response => {
        if (response.data.status === 0) {
          this.userOrderList = response.data.orders
        } else {
          this.$message.error('订单号错误')
          this.userOrderList = []
        }
      })
    },
    flipOver: function(page) {
      let _end = this.pageSize * page
      let end = this.totalNumber < (_end) ? this.totalNumber : _end
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
        this.totalNumber = this.list.length
        let totalNumber = this.totalNumber
        this.userOrderList = []
        let size = this.pageSize
        if (totalNumber < size) {
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
  .search-order {
    width: 300px;
    margin-left: 50px;
    margin-bottom: 60px;
  }
  .search-box {
    width: 70%;
  }
  .order-head {
    font-size: 20px;
    color:black;
    font-weight: bold;
    margin-bottom: 30px;
  }
  .order-table {
    margin-left: 3%;
    width: 100%;
    margin-bottom: 50px;
  }
  .really-table {
    margin-bottom: 50px;
  }
  .first-div {
    width: 80%;
    margin: 50px auto;
    text-align: center;
  }
  .pager {
    text-align: center
  }
  .list-table {
    width: 100%;
  }
</style>
