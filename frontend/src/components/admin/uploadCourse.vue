<template>
  <div class="upload-page">
    <div class="upload-inner">
      <el-form :v-model="update_form" style="text-align: center;">

        <el-form-item label="课程标题：" label-width="120px">
          <el-col :span="18">
            <el-input v-model="update_form.course_title" auto-complete="true" placeholder="请输入内容" clearable required="required"></el-input>
          </el-col>
        </el-form-item>

        <el-form-item label="课程简介：" label-width="120px">
          <el-col :span="18">
            <el-input type="textarea" :autosize="{ minRows: 3, maxRows: 5}" auto-complete="true" placeholder="请输入内容" v-model="update_form.course_description" clearable required="required"></el-input>
          </el-col>
        </el-form-item>

        <el-form-item label="上传音频：" label-width="120px" style="text-align:left">
          <el-col :span="18">
            <el-upload class="upload-demo" action="upload_audio_URL" :on-change="handleChange" :before-upload="beforeUpload" :file-list="update_form.audioList">
              <el-button size="small" type="primary">点击上传</el-button>
              <div slot="tip" class="el-upload__tip">只能上传mp3/wav文件</div>
            </el-upload>
          </el-col>
        </el-form-item>

        <el-form-item label="上传图片：" label-width="120px" style="text-align:left">
          <el-col :span="18">
            <el-upload
              action="upload_pic_URL"
              list-type="picture-card"
              :on-preview="handlePictureCardPreview">
              <i class="el-icon-plus"></i>
            </el-upload>
            <el-dialog :visible.sync="dialogVisible">
              <img width="100%" :src="dialogImageUrl" alt="">
            </el-dialog>
          </el-col>
        </el-form-item>

        <el-form-item label="图片显示时间：" label-width="120px">
          <el-col :span="18">
            <el-input type="textarea" :autosize="{ minRows: 3, maxRows: 5}" auto-complete="true" placeholder="请输入每张图片开始播放的时间，格式为: 01:25(1分25秒)，每个时间以空格分隔" v-model="update_form.timelist" clearable required="required"></el-input>
          </el-col>
        </el-form-item>

        <el-form-item label="课程内容：" label-width="120px">
          <el-col :span="18">
            <el-input type="textarea" :autosize="{ minRows: 5, maxRows: 10}" auto-complete="true" placeholder="请输入内容" v-model="update_form.course_contain" clearable required="required"></el-input>
          </el-col>
        </el-form-item>

        <el-form-item label="" label-width="120px" style="text-align:left">
          <el-col :span="18">
            <el-checkbox v-model="update_form.message_right">开放留言区</el-checkbox>
          </el-col>
        </el-form-item>

        <el-form-item label="价格：" label-width="120px" style="text-align:left;width:250px">
          <el-row :span="18" style="width:300px">
            <el-input v-model="update_form.price" auto-complete="true" required="required" style="width:100px"></el-input>
          </el-row>
        </el-form-item>

        <el-form-item label="焚毁时间：" label-width="120px" style="text-align:left;width:250px">
          <el-col :span="18">
            <el-input v-model="update_form.destroy_time" auto-complete="true" required="required" style="width:100px"></el-input>
          </el-col>
        </el-form-item>

        <el-form-item style="text-align:right">
          <br />
          <el-button type="primary" icon="el-icon-upload">上传课程</el-button>
          <el-button icon="el-icon-delete" @click="clearpage">清空</el-button>
          <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      update_form: {
        course_title: '',
        course_description: '',
        timelist: '',
        course_contain: '',
        message_right: true,
        price: 0,
        destroy_time: 0,
        audioList: []
      },
      // uploadURL 为上传动作的后端接口
      upload_audio_URL: '',
      upload_pic_URL: '',
      dialogImageUrl: '',
      dialogVisible: false
    }
  },
  methods: {
    beforeUpload(file) {
      if (['audio/mp3', 'audio/wav'].indexOf(file.type) === -1) {
        this.$message.error('请上传正确的音频格式')
        return false
      }
    },
    handleChange(file, audioList) {
      this.audioList = audioList.slice(-1)
    },
    handleRemove(file, fileList) {
    },
    handlePictureCardPreview(file) {
      this.dialogImageUrl = file.url
      this.dialogVisible = true
    },
    clearpage() {
      this.update_form.course_title = ''
      this.update_form.course_description = ''
      this.update_form.timelist = ''
      this.update_form.course_contain = ''
      this.update_form.message_right = true
      this.update_form.price = 0
      this.update_form.destroy_time = 0
      this.update_form.audioList = []
    }
  }
}
</script>

<style scoped>
  .upload-page {
    text-align: center;
    position: absolute;
    margin: auto 100px;
  }
  .upload-inner {
    width:1000px;
    text-align: center;
    margin: 0 auto;
  }
</style>
