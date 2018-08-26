<template>
<div>
  <div class="data-block">
    <h1>近期浏览</h1>
    <div class="confirm-div">
      近&nbsp;<el-input class="browse-check" v-model="dayBrowse" placeholder="7"></el-input>
      &nbsp;天&nbsp;&nbsp;&nbsp;&nbsp;
      <el-button type="primary" @click="browseClick">确定</el-button>
    </div>
    <div id="browse-chart"></div>
  </div>
  <div class="data-block">
    <h1>近期支付</h1>
    <div class="confirm-div">
      近&nbsp;<el-input class="browse-check" v-model="dayPay" placeholder="8"></el-input>
      &nbsp;天&nbsp;&nbsp;&nbsp;&nbsp;
      <el-button type="primary" @click="payClick">确定</el-button>
    </div>
    <div id="pay-chart"></div>
  </div>
</div>
</template>

<script>
import * as utils from '../utils/utils.js'
import echarts from 'echarts'
import axios from 'axios'
import qs from 'qs'

export default {
  data() {
    return {
      browseData: [5, 20, 36, 10, 10, 20, 7],
      payData: [],
      dayBrowse: 7,
      dayPay: 8,
      dayOfBrowse: [],
      dayOfPay: []
    }
  },
  mounted() {
    this.getBrows()
    this.getOrders()
  },
  methods: {
    getBrows() {
      axios.post(utils.getURL() + 'api/getpv/', qs.stringify({
        days: this.dayBrowse
      })).then(response => {
        if (response.data.status === 0) {
          this.browseData = response.data.PV_list
          this.dayOfBrowse = response.data.time
          this.drawBrowseChart()
        } else {
          alert('内部错误')
        }
      })
    },
    getOrders() {
      axios.post(utils.getURL() + 'api/getvol/', qs.stringify({
        days: this.dayPay
      })).then(response => {
        if (response.data.status === 0) {
          this.payData = response.data.VOL_list
          this.dayOfPay = response.data.time
          this.drawPayChart()
        } else {
          alert('内部错误')
        }
      })
    },
    drawBrowseChart() {
      let browseChart = echarts.init(document.getElementById('browse-chart'))
      browseChart.setOption({
        title: { text: '近' + this.dayBrowse + '天浏览情况' },
        tooltip: {},
        xAxis: {
          data: this.dayOfBrowse
        },
        yAxis: {},
        series: [{
          name: '人数/人',
          type: 'bar',
          data: this.browseData,
          itemStyle: {color: 'skyblue'}
        }]
      })
    },
    drawPayChart() {
      let payChart = echarts.init(document.getElementById('pay-chart'))
      payChart.setOption({
        title: { text: '近' + this.dayPay + '天支付情况' },
        tooltip: {},
        xAxis: {
          data: this.dayOfPay
        },
        yAxis: {},
        series: [{
          name: '人数/人',
          type: 'bar',
          data: this.payData,
          itemStyle: {color: 'skyblue'}
        }]
      })
    },
    browseClick() {
      if (this.dayBrowse === '') {
        this.dayBrowse = 7
      }
      this.getBrows()
    },
    payClick() {
      if (this.dayPay === '') {
        this.dayPay = 8
      }
      this.getOrders()
    }
  },
  created: function() {
    this.dayOfBrowse = []
    this.browseData = []
    this.dayOfPay = []
    this.payData = []
    this.dayBrowse = 7
    this.dayPay = 7
  }
}
</script>
<style scoped>
  .data-block {
    width: 90%;
    height: 400px;
    text-align: left;
    margin-left: 5%;
    margin-bottom: 10%;
  }

  h1 {
    color: black;
  }

  .confirm-div {
    color: black;
    margin-left: 1%;
  }

  .browse-check {
    width: 60px;
    margin-bottom: 3%;
    position: relative;
  }

  #browse-chart {
    width: 60%;
    height: 100%;
  }

  #pay-chart {
    width: 60%;
    height: 100%;
  }
</style>
