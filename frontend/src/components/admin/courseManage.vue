<template>
<div class="course-manage">

  <div id="search-course">
    <el-row :gutter="20">
      <el-col :span="6" :offset="15">
        <el-input v-model="searchId" placeholder="请输入课程编号">
        </el-input>
      </el-col>
      <el-col :span="2">
        <el-button type="primary" icon="el-icon-search" @click="search">
          搜索
        </el-button>
      </el-col>
    </el-row>
  </div>

  <div id="course-list">
    <el-table :data="courseData" border class="course-table">
      <el-table-column
        type="index"
        :index="indexMethod"
        header-align=center>
      </el-table-column>
      <el-table-column
        prop="courseId"
        label="课程编号"
        width="180"
        header-align=center>
      </el-table-column>
      <el-table-column
        prop="courseTitle"
        label="课程标题"
        width="220"
        header-align=center>
      </el-table-column>
      <el-table-column
        prop="destroyTime"
        label="焚毁时间"
        width="130"
        header-align=center>
      </el-table-column>
      <el-table-column
        header-align=center
        prop="messageRight"
        label="留言区是否开放"
        width="130"
        :formatter="messageRightCal"
        show-overflow-tooltip>
      </el-table-column>
      <el-table-column
        prop="coursePrice"
        label="课程价格"
        width="130"
        header-align=center>
      </el-table-column>
      <el-table-column label="操作" header-align=center>
        <template slot-scope="scope">
          <router-link :to="{
            name:'coursepage',
            params:{courseid: courseData[scope.$index].courseId}}">
            <el-button type="text" size="small">查看</el-button>
          </router-link>
          <router-link :to="{
            name:'editCourse',
            params:{courseId: courseData[scope.$index].courseId}}">
          <el-button type="text" size="small" >编辑</el-button>
          </router-link>
        </template>
      </el-table-column>
    </el-table>
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
      searchId: '',
      courseData: [
        {
          courseId: 15222,
          courseTitle: '我们爱科学',
          destroyTime: 8,
          messageRight: true,
          coursePrice: 25
        },
        {
          courseId: 15223,
          courseTitle: '我们爱学习',
          destroyTime: 10,
          messageRight: false,
          coursePrice: 20
        }
      ],
      editVisible: false,
      index: 0,
      editIndex: 0
    }
  },
  methods: {
    indexMethod(index) {
      return index + 1
    },
    messageRightCal(data) {
      return data.messageRight ? '开放' : '关闭'
    },
    getList() {
      axios.post(utils.getURL() + 'api/showcourse/', qs.stringify({
        searchId: this.searchId
      })).then(response => {
        if (response.data.status === 0) {
          this.courseData = response.data.courseData
        } else {
          this.$message.error('搜索错误')
        }
      })
    },
    search() {
      this.getList()
    }
  },
  created: function() {
    this.getList()
  }
}
</script>

<style scoped>
.course-manage {
  width: 80%;
  margin: 20px 5%;
}
#search-course {
  width: 100%;
  margin: 0 auto;
}
#course-list {
  width: 950px;
  height: 1000px;
  margin: 50px auto;
}
.course-table {
  width: 100%;
}
</style>
