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
            <el-upload
              class="upload-demo"
              :action="upload_audio_URL()"
              :on-success="audioResponse"
              :data="update_form"
              :on-change="handleChange"
              :before-upload="beforeUpload"
              :file-list="update_form.audioList">
              <el-button size="small" type="primary">点击上传</el-button>
              <div slot="tip" class="el-upload__tip">只能上传mp3/wav文件</div>
            </el-upload>
          </el-col>
        </el-form-item>

        <el-form-item label="上传图片：" label-width="120px" style="text-align:left">
          <el-col :span="18">
            <el-upload
              :action="upload_pic_URL()"
              :on-success="pictureResponse"
              :data="update_form"
              list-type="picture-card"
              :file-list="update_form.imgList"
              :on-preview="handlePictureCardPreview">
              <i class="el-icon-plus"></i>
            </el-upload>
            <el-dialog :visible.sync="dialogVisible">
              <img width="100%" :src="dialogImageUrl" alt="">
            </el-dialog>
          </el-col>
        </el-form-item>

        <el-form-item label="图片显示时间：" label-width="120px" style="text-align:left">
          <el-col :span="3">
            <el-dropdown @command="handleCommand">
              <span class="el-dropdown-link">
                {{dropdownMessage}}<i class="el-icon-arrow-down el-icon--right"></i>
              </span>
              <el-dropdown-menu slot="dropdown">
                <el-dropdown-item v-for="(item, index) in update_form.imgInfo" :key="item.id" :command="index + 1">
                  图片{{ index + 1 }}
                </el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
          </el-col>
          <el-col :span="3">
            <el-input auto-complete="true" placeholder="0" style="width:80px" v-model="miniteCache"></el-input>
            <span class="time">分</span>
          </el-col>
          <el-col :span="3">
            <el-input auto-complete="true" placeholder="0" style="width:80px" v-model="secondeCache"></el-input>
            <span class="time">秒</span>
          </el-col>
          <el-col :span="3" :offset="1">
            <el-button type="primary" @click="getTime">确定</el-button>
          </el-col>
        </el-form-item>

        <el-form-item label="课程内容：" label-width="120px">
          <el-col :span="18">
            <el-input type="textarea" :autosize="{ minRows: 5, maxRows: 10}" auto-complete="true" placeholder="请输入内容" v-model="update_form.course_contain" clearable required="required"></el-input>
          </el-col>
        </el-form-item>

        <el-form-item label="" label-width="120px" style="text-align:left">
          <el-col :span="18">
            <el-checkbox v-model="update_form.message_on">开放留言区</el-checkbox>
          </el-col>
        </el-form-item>

        <el-form-item label="价格：" label-width="120px" style="text-align:left;width:250px">
          <el-row :span="18" style="width:300px">
            <el-input v-model="update_form.price" auto-complete="true" required="required" style="width:100px"></el-input>
          </el-row>
        </el-form-item>

        <el-form-item label="赏金比例：" label-width="120px" style="text-align:left;width:250px" v-if="update_form.price!=0">
          <el-row :span="18" style="width:300px">
            <el-input v-model="update_form.percentage" auto-complete="true" style="width:100px"></el-input>
          </el-row>
        </el-form-item>

        <el-form-item label="焚毁时间：" label-width="120px" style="text-align:left;width:250px">
          <el-col :span="18">
            <el-input v-model="update_form.destroy_time" auto-complete="true" required="required" style="width:100px"></el-input>
          </el-col>
        </el-form-item>

        <el-form-item style="text-align:right">
          <br />
          <el-button type="primary" @click="uploadcourse" icon="el-icon-upload">上传课程</el-button>
          <el-button icon="el-icon-delete" @click="clearpage" class="clear">清空</el-button>
          <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import qs from 'qs'
import axios from 'axios'
import * as utils from '../utils/utils.js'

export default {
  data() {
    return {
      update_form: {
        mark: '',
        course_title: '',
        course_description: '',
        timelist: [],
        course_contain: '',
        messageOn: true,
        price: 0,
        destroy_time: 0,
        audioId: NaN,
        audioList: [],
        imgList: [],
        imgInfo: [],
        pictureIndex: -1,
        percentage: 0
      },
      // uploadURL 为上传动作的后端接口
      dialogImageUrl: '',
      dialogVisible: false,
      input: '',
      dropdownMessage: '选择图片',
      miniteCache: 0,
      secondeCache: 0
    }
  },
  methods: {
    getTime() {
      let minite = 0
      let seconde = 0
      let secondes
      if (typeof this.pictureIndex === 'undefined') {
        alert('请选择图片')
        return
      }
      try {
        alert(typeof this.secondeCache)
        if (this.miniteCache) {
          minite = this.miniteCache
        }
        if (this.secondeCache) {
          seconde = this.secondeCache
        }
        secondes = minite * 60 + seconde
        this.imgInfo[this.pictureIndex].start = secondes
      } catch (err) {
        alert('请输入正确时间')
      }
      alert(this.imgInfo[this.pictureIndex].start)
    },
    audioResponse(response) {
      this.update_form.audioId = response.id
    },
    pictureResponse(response) {
      this.update_form.imgInfo.push({id: response.id, start: 0})
    },
    upload_audio_URL() {
      return utils.getURL() + 'api/uploadaudio/'
    },
    upload_pic_URL() {
      return utils.getURL() + 'api/uploadcoursepicture/'
    },
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
      this.update_form.message_on = true
      this.update_form.price = 0
      this.update_form.destroy_time = 0
      this.update_form.audioList = []
    },
    addTime() {
    },
    handleCommand(command) {
      this.pictureIndex = command - 1
      this.dropdownMessage = '图片' + command
    },
    uploadcourse() {
      axios.post(utils.getURL() + 'api/uploadcourse/', qs.stringify({
        updateForm: JSON.stringify(this.update_form)
      })).then(response => {
        if (response.data.status === 0) {
          alert('创建成功')
          location.replace()
        } else {
          alert('ERROR!')
        }
      })
    }
  },
  created: function() {
    this.update_form.mark = (new Date()).valueOf()
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
    /* text-align: center; */
    margin: 0 auto;
  }
  .el-form-item__content {
    text-align: left !important;
  }
  .time {
    color: black;
    font-size: 16px;
  }
</style>
