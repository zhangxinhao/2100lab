<template>
<div>
  <div class="datablock">
    <h1>近期浏览</h1>
    <div class="confirm_div">
      近&nbsp;<el-input class="browse_check" v-model="day_browse" placeholder="7"></el-input>&nbsp;天&nbsp;&nbsp;&nbsp;&nbsp;
      <el-button type="primary" @click="browseClick">确定</el-button>
    </div>
    <div id="browse_chart"></div>
  </div>
  <div class="datablock">
    <h1>近期支付</h1>
    <div class="confirm_div">
      近&nbsp;<el-input class="browse_check" v-model="day_pay" placeholder="8"></el-input>&nbsp;天&nbsp;&nbsp;&nbsp;&nbsp;
      <el-button type="primary" @click="payClick">确定</el-button>
    </div>
    <div id="pay_chart"></div>
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
      day_browse: 7,
      day_pay: 8,
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
        days: this.day_browse
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
        days: this.day_pay
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
      let browseChart = echarts.init(document.getElementById('browse_chart'))
      browseChart.setOption({
        title: { text: '近' + this.day_browse + '天浏览情况' },
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
      let payChart = echarts.init(document.getElementById('pay_chart'))
      payChart.setOption({
        title: { text: '近' + this.day_pay + '天支付情况' },
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
      if (this.day_browse === '') {
        this.day_browse = 7
      }
      this.getBrows()
    },
    payClick() {
      if (this.day_pay === '') {
        this.day_pay = 8
      }
      this.getOrders()
    }
  },
  created: function() {
    this.dayOfBrowse = []
    this.browseData = []
    this.dayOfPay = []
    this.payData = []
    this.day_browse = 7
    this.day_pay = 7
  }
}
</script>
<style scoped>
  .datablock {
    width: 90%;
    height: 400px;
    text-align: left;
    margin-left: 5%;
    margin-bottom: 10%;
  }

  h1 {
    color: black;
  }

  .confirm_div {
    color: black;
    margin-left: 1%;
  }

  .browse_check {
    width: 60px;
    margin-bottom: 3%;
    position: relative;
  }

  #browse_chart {
    width: 60%;
    height: 100%;
  }

  #pay_chart {
    width: 60%;
    height: 100%;
  }

</style>
