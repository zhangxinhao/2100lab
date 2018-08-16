<template>
  <div>
    <div class="browsTitle">
      <div class="browsHead">浏览历史</div>
      <hr />
      <div v-for="brow in browList" :key="brow.courseTitle">
        <el-container>
          <el-aside>
            <div class="browPicture">
              <img :alt="brow.courseTitle" :src="brow.pictureSrc" width="300" height="200"/>
            </div>
          </el-aside>
          <el-main>
            <div class="browTitle">课程：{{ brow.courseTitle }}</div>
            <div class="browLastTime">上次浏览时间：{{ brow.lastBrowTime }}</div>
          </el-main>
        </el-container>
      </div>

        <!-- 每页显示六条记录 page-size -->
        <!-- 最多显示八个页面按钮 page-count -->
      <div style="text-align:right">
        <el-pagination
          background
          layout="prev, pager, next"
          :total="browpages"
          page-size=6
          :current-page.sync="nowPage"
          :pager-count=6
          >
        </el-pagination>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  data() {
    return {
      browList: [
        {pictureSrc: require('../assets/read.jpg'), courseTitle: '春眠不觉晓', lastBrowTime: '2018-3-5'},
        {pictureSrc: require('../assets/read.jpg'), courseTitle: '处处闻啼鸟', lastBrowTime: '2018-3-5'},
        {pictureSrc: require('../assets/read.jpg'), courseTitle: '夜来风雨声', lastBrowTime: '2018-3-5'},
        {pictureSrc: require('../assets/read.jpg'), courseTitle: '花落知多少', lastBrowTime: '2018-3-5'},
        {pictureSrc: require('../assets/read.jpg'), courseTitle: '少壮不努力', lastBrowTime: '2018-3-5'},
        {pictureSrc: require('../assets/read.jpg'), courseTitle: '老大徒伤悲', lastBrowTime: '2018-3-5'}
      ],
      // 总共有多少记录
      browpages: 200,
      // 设置当前处于哪个页面按钮上
      nowPage: 1
    }
  },
  methods: {
    handleChange(value) {
      console.log(value)
    }
  },
  mounted: function() {
    axios.post('http://192.168.55.33:8000/api/listrecentvisit/').then(
        response => {
          console.log(response)
        }
      )
  }
}
</script>
<style>
</style>
