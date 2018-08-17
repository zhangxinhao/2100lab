<template>
  <div>
    <div>
      <div>已购课程</div>
      <hr />
      <div v-for="bill in billList" :key="bill.courseTitle">
        <el-container class="text">
          <el-aside>
            <div class="billpicture">
              <img :alt="bill.courseTitle" :src="bill.pictureSrc" style="width: 100%; height: 100%; object-fit: contain;"/>
            </div>
          </el-aside>
          <el-main>
            <div>课程：{{ bill.courseTitle }}</div>
            <div>上次浏览时间：{{ bill.lastBillTime }}</div>
          </el-main>
        </el-container>
      </div>

        <!-- 每页显示六条记录 page-size -->
        <!-- 最多显示八个页面按钮 page-count -->
      <div style="text-align:right">
        <el-pagination
          background
          layout="prev, pager, next"
          :total="billpages"
          page-size="6"
          :current-page.sync="nowPage"
          :pager-count="6"
          >
        </el-pagination>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      billList: [
        {pictureSrc: require('../assets/p_course.jpg'), courseTitle: '小雨晨光内', lastBillTime: '2018-3-5'},
        {pictureSrc: require('../assets/p_course.jpg'), courseTitle: '初来叶上闻', lastBillTime: '2018-3-5'},
        {pictureSrc: require('../assets/p_course.jpg'), courseTitle: '雾交才洒地', lastBillTime: '2018-3-5'},
        {pictureSrc: require('../assets/p_course.jpg'), courseTitle: '风逆旋随云', lastBillTime: '2018-3-5'},
        {pictureSrc: require('../assets/p_course.jpg'), courseTitle: '暂起柴荆色', lastBillTime: '2018-3-5'},
        {pictureSrc: require('../assets/p_course.jpg'), courseTitle: '轻沾鸟兽群', lastBillTime: '2018-3-5'},
        {pictureSrc: require('../assets/p_course.jpg'), courseTitle: '麝香山一半', lastBillTime: '2018-3-5'},
        {pictureSrc: require('../assets/p_course.jpg'), courseTitle: '亭午未全分', lastBillTime: '2018-3-5'}
      ],
      // 总共有多少记录
      billpages: 200,
      // 设置当前处于哪个页面按钮上
      nowPage: 1
    }
  },
  methods: {
    handleChange(value) {
      console.log(value)
    }
  }
}
</script>
<style scoped>
  .text {
    background-color: darkgray;
    border: 1px solid black;
    margin-bottom: 1%;
  }

  .billpicture {
    width: 94%;
    height: 200px;
    margin: 3%;
  }

</style>
