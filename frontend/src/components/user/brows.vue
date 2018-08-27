<template>
  <div class="first-div">
    <div class="title">
      <div class="brows-head">浏览历史</div>
      <div v-for="brow in browList" :key="brow.courseTitle">
        <el-container class="contain">
          <el-aside>
            <div class="picture-div">
              <img
                :alt="brow.courseTitle"
                :src="brow.pictureSrc"
                width=90%
                height=90%/>
            </div>
          </el-aside>
          <el-main class="my-main">
            <div class="brow-title">课程：{{ brow.courseTitle }}</div>
            <div class="brow-last">
              上次浏览时间：{{ brow.lastBrowTime }}
            </div>
          </el-main>
        </el-container>
      </div>
        <!-- 每页显示六条记录 page-size -->
        <!-- 最多显示多少个个页面按钮 page-count -->
      <div>
        <el-pagination
          background
          small
          layout="prev, pager, next"
          :page-size="pageSize"
          :total="totalNumber"
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
        {
          pictureSrc: require('../../assets/class2.jpg'),
          courseTitle: '春眠不觉晓',
          lastBrowTime: '2018-3-5'
        },
        {
          pictureSrc: require('../../assets/read.jpg'),
          courseTitle: '处处闻啼鸟',
          lastBrowTime: '2018-3-5'
        },
        {
          pictureSrc: require('../../assets/read.jpg'),
          courseTitle: '夜来风雨声',
          lastBrowTime: '2018-3-5'
        },
        {
          pictureSrc: require('../../assets/read.jpg'),
          courseTitle: '花落知多少',
          lastBrowTime: '2018-3-5'
        },
        {
          pictureSrc: require('../../assets/read.jpg'),
          courseTitle: '少壮不努力',
          lastBrowTime: '2018-3-5'
        },
        {
          pictureSrc: require('../../assets/read.jpg'),
          courseTitle: '老大徒伤悲',
          lastBrowTime: '2018-3-5'
        }
      ],
      courses: [],
      pageSize: 12,
      totalNumber: 100,
      pageNo: 1
    }
  },
  methods: {
    flipeOver: function (page) {
      let totalEnd = this.pageSize * page
      let end = this.totalNumber < (totalEnd) ? this.totalNumber : totalEnd
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
      this.totalNumber = this.courses.length
      let totalNumber = this.totalNumber
      this.browList = []
      let size = this.pageSize
      if (totalNumber < size) {
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
  .brows-head {
    font-weight: bold;
    font-size: 18px;
    margin-bottom: 50px;
  }
  .first-div {
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
  .picture-div {
    width: 250px;
    height: 180px;
    margin: auto;
    text-align: center;
  }
  .brow-title {
    font-size: 15px;
    margin-bottom: 20%;
    margin-top: 10%;
  }
  .brow-last {
    font-size: 12px;
    color: darkgray;
  }
   @media screen and (max-width: 500px) {
    .picture-div {
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
    .brow-title {
      font-size: 12px;
      margin-top: 10%;
      margin-bottom: 10%;
    }
    .brow-last {
      font-size: 7px;
      color: darkgray;
    }
    .my-main {
      padding: 0px;
    }
  }
</style>
