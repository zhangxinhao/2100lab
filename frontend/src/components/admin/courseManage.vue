<template>
<div class="course-manage">

  <div id="search-course">
    <el-row :gutter="20">
      <el-col :span="6" :offset="15"><el-input v-model="courseId" placeholder="请输入课程编号"></el-input></el-col>
      <el-col :span="2"><el-button type="primary" icon="el-icon-search">搜索</el-button></el-col>
    </el-row>
  </div>

  <div id="course-list">
    <el-table :data="courseData" border style="width: 100%">
      <el-table-column type="index" :index="indexMethod"></el-table-column>
      <el-table-column prop="courseId" label="课程编号" width="180"></el-table-column>
      <el-table-column prop="courseTitle" label="课程标题" width="220"></el-table-column>
      <el-table-column prop="destroyTime" label="焚毁时间" width="130"></el-table-column>
      <el-table-column prop="messageRight" label="留言区是否开放" width="130"  :formatter="messageRightCal" show-overflow-tooltip></el-table-column>
      <el-table-column prop="coursePrice" label="课程价格" width="130"></el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button type="text" size="small">查看</el-button>
          <el-button type="text" size="small" @click="editFunction(scope.$index)">编辑</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>

  <div class="editDialog">
    <el-dialog title="编辑" :visible.sync="editVisible" width="400px" height="700px">
      <el-form :model="courseData[editIndex]">

        <el-form-item label="焚毁时间" label-width="120px" prop="destroyTime">
          <el-col :span="18">
            <el-input v-model="courseData[editIndex].destroyTime" auto-complete="true" style="width:100px"></el-input>
          </el-col>
        </el-form-item>

        <el-form-item label="价格" label-width="120px">
          <el-row :span="18" style="width:300px">
            <el-input v-model="courseData[editIndex].coursePrice" auto-complete="true" style="width:100px"></el-input>
          </el-row>
        </el-form-item>

        <el-form-item label="" label-width="120px">
          <el-col :span="18">
            <el-checkbox v-model="courseData[editIndex].messageRight">开放留言区</el-checkbox>
          </el-col>
        </el-form-item>

      </el-form>
      <div slot="footer" class="edit-footer">
        <el-button @click="editVisible = false">取 消</el-button>
        <el-button type="primary" @click="edit">确 定</el-button>
      </div>
    </el-dialog>
  </div>

</div>
</template>

<script>
export default {
  data() {
    return {
      courseId: '',
      courseData: [
        {courseId: 15222, courseTitle: '我们爱科学', destroyTime: 8, messageRight: true, coursePrice: 25},
        {courseId: 15223, courseTitle: '我们爱学习', destroyTime: 10, messageRight: false, coursePrice: 20}
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
    editFunction(editIndex) {
      this.editVisible = true
      console.log(editIndex)
      this.editIndex = editIndex
    },
    edit() {
      this.editVisible = false
    },
    messageRightCal(data) {
      return data.messageRight ? '开放' : '关闭'
    }
  }
}
</script>

<style scoped>
.course-manage {
  width: 1020px;
  margin: 20px auto;
}
#search-course {
  width: 1000px;
}
#course-list {
  width: 950px;
  height: 1000px;
  margin: 50px auto;
}
</style>
