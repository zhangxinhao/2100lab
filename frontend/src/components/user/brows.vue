<template>
  <div class="firstdiv">
    <div class="title">
      <div class="browshead">浏览历史</div>
      <div v-for="brow in browList" :key="brow.courseTitle">
        <el-container class="contain">
          <el-aside class="myside">
            <div class="picturediv">
              <img :alt="brow.courseTitle" :src="brow.pictureSrc" width=90% height=90%/>
            </div>
          </el-aside>
          <el-main class="mymain">
            <div class="browtitle">课程：{{ brow.courseTitle }}</div>
            <div class="browlasttime">上次浏览时间：{{ brow.lastBrowTime }}</div>
          </el-main>
        </el-container>
      </div>
        <!-- 每页显示六条记录 page-size -->
        <!-- 最多显示八个页面按钮 page-count -->
      <div>
        <el-pagination
          background
          small
          layout="prev, pager, next"
          :page-size="pageSize"
          :total="totalnumber"
          :current-page.sync="pageNo"
          :pager-count="7"
          @current-change="flipeOver">
        </el-pagination>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
import * as utils from '../utils/utils.js'
import qs from 'qs'

export default {
  data() {
    return {
      browList: [
        {pictureSrc: require('../../assets/class2.jpg'), courseTitle: '春眠不觉晓', lastBrowTime: '2018-3-5'},
        {pictureSrc: require('../../assets/read.jpg'), courseTitle: '处处闻啼鸟', lastBrowTime: '2018-3-5'},
        {pictureSrc: require('../../assets/read.jpg'), courseTitle: '夜来风雨声', lastBrowTime: '2018-3-5'},
        {pictureSrc: require('../../assets/read.jpg'), courseTitle: '花落知多少', lastBrowTime: '2018-3-5'},
        {pictureSrc: require('../../assets/read.jpg'), courseTitle: '少壮不努力', lastBrowTime: '2018-3-5'},
        {pictureSrc: require('../../assets/read.jpg'), courseTitle: '老大徒伤悲', lastBrowTime: '2018-3-5'}
      ],
      courses: [],
      pageSize: 12,
      totalnumber: 100,
      pageNo: 1
    }
  },
  methods: {
    handleChange(value) {
    },
    flipeOver: function (page) {
      let _end = this.pageSize * page
      let end = this.totalnumber < (_end) ? this.totalnumber : _end
      this.browList = []
      let start = this.pageSize * (page - 1)
      for (let i = start; i < end; i++) {
        this.browList.push(this.courses[i])
      }
    }
  },
  created: function() {
    axios.post(utils.getURL() + 'api/listrecentvisit/', qs.stringify({
      id: this.$route.params.userid
    })).then(response => {
      this.courses = response.data.courses
      this.totalnumber = this.courses.length
      let totalnumber = this.totalnumber
      this.browList = []
      let size = this.pageSize
      if (totalnumber < size) {
        this.browList = this.courses
      } else {
        for (let i = 0; i < size; i++) {
          this.browList.push(this.courses[i])
        }
      }
    })
  }
}
</script>
<style scoped>
  .browshead {
    font-weight: bold;
    font-size: 18px;
    margin-bottom: 50px;
  }
  .firstdiv {
    width: 100%;
  }
  .title {
    width: 100%;
  }
  .contain {
    margin-bottom: 30px !important;
    width: 50%;
    margin: 0px auto;
    text-align: center;
  }
  .el-aside {
    width: 100%;
  }
  .picturediv {
    width: 250px;
    height: 180px;
    margin: auto;
    text-align: center;
  }
  .browtitle {
    font-size: 15px;
    margin-bottom: 20%;
    margin-top: 10%;
  }
  .browlasttime {
    font-size: 12px;
    color: darkgray;
  }
   @media screen and (max-width: 500px) {
    .picturediv {
      width: 130px;
      height: 90px;
      margin: 0px;
      text-align: center;
    }
    .contain {
      margin-bottom: 3px !important;
      width: 100%;
      margin: 0px auto;
      text-align: center;
    }
    .el-aside {
      width: 130px !important;
    }
    .browtitle {
      font-size: 12px;
      margin-top: 10%;
      margin-bottom: 10%;
    }
    .browlasttime {
      font-size: 7px;
      color: darkgray;
    }
    .mymain {
      padding: 0px;
    }
  }
</style>
