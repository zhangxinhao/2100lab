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
import echarts from 'echarts'

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
    this.drawBrowseChart()
    this.drawPayChart()
  },
  methods: {
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
      this.dayOfBrowse = []
      this.browseData = []
      for (let i = this.day_browse; i >= 1; i--) {
        this.dayOfBrowse.push(i)
        this.browseData.push(i * 14927 % 121)
      }
      this.drawBrowseChart()
    },
    payClick() {
      if (this.day_pay === '') {
        this.day_pay = 8
      }
      this.dayOfPay = []
      this.payData = []
      for (let i = this.day_pay; i >= 1; i--) {
        this.dayOfPay.push(i)
        this.payData.push(i * 14927 % 37)
      }
      this.drawPayChart()
    }
  },
  created: function() {
    this.dayOfBrowse = []
    this.browseData = []
    this.dayOfPay = []
    this.payData = []
    for (let i = this.day_browse; i >= 1; i--) {
      this.dayOfBrowse.push(i)
      this.browseData.push(i * 14927 % 121)
    }
    for (let i = this.day_pay; i >= 1; i--) {
      this.dayOfPay.push(i)
      this.payData.push(i * 14927 % 37)
    }
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
