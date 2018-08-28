<template>
  <div class="upload-page">
    <div class="upload-inner">
      <el-form :v-model="updateForm" class="update-form">

        <el-form-item label="课程标题：" label-width="120px">
          <el-col :span="18">
            <el-input v-model="updateForm.courseTitle"
              auto-complete="true" placeholder="请输入内容"
              clearable required="required">
            </el-input>
          </el-col>
        </el-form-item>

        <el-form-item label="课程简介：" label-width="120px">
          <el-col :span="18">
            <el-input type="textarea" :autosize="{ minRows: 3, maxRows: 5}"
              auto-complete="true"
              placeholder="请输入内容"
              v-model="updateForm.courseDescription"
              clearable required="required">
            </el-input>
          </el-col>
        </el-form-item>

        <el-form-item
          label="上传音频："
          label-width="120px"
          class="update-form-item">
          <el-col :span="18">
            <el-upload
              class="upload-demo"
              :action="upload_audio_URL()"
              :on-success="audioResponse"
              :data="updateForm"
              :on-change="handleChange"
              :before-upload="beforeUpload"
              :file-list="updateForm.audioList">
              <el-button size="small" type="primary">点击上传</el-button>
              <div slot="tip" class="el-upload__tip">只能上传mp3/wav文件</div>
            </el-upload>
          </el-col>
        </el-form-item>

        <el-form-item
          label="上传图片："
          label-width="120px"
          class="update-form-item">
          <el-col :span="18">
            <el-upload
              :action="upload_pic_URL()"
              :on-success="pictureResponse"
              :data="updateForm"
              list-type="picture-card"
              :file-list="updateForm.imgList"
              :on-preview="handlePictureCardPreview">
              <i class="el-icon-plus"></i>
            </el-upload>
            <el-dialog :visible.sync="dialogVisible">
              <img width="100%" :src="dialogImageUrl" alt="">
            </el-dialog>
          </el-col>
        </el-form-item>

        <el-form-item
          label="图片显示时间："
          label-width="120px"
          class="update-form-item">
          <el-col :span="3">
            <el-dropdown @command="handleCommand">
              <span class="el-dropdown-link">
                {{ dropdownMessage }}
                <i class="el-icon-arrow-down el-icon--right"></i>
              </span>
              <el-dropdown-menu slot="dropdown">
                <el-dropdown-item
                  v-for="(item, index) in updateForm.imgInfo"
                  :key="item.id"
                  :command="index + 1">
                  图片{{ index + 1 }}
                </el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
          </el-col>
          <el-col :span="3">
            <el-input
              auto-complete="true"
              :placeholder="miniteTemp"
              class="time-input"
              v-model="miniteTemp">
            </el-input>
            <span class="time">分</span>
          </el-col>
          <el-col :span="3">
            <el-input
              auto-complete="true"
              :placeholder="secondeTemp"
              class="time-input"
              v-model="secondeTemp">
            </el-input>
            <span class="time">秒</span>
          </el-col>
          <el-col :span="3" :offset="1">
            <el-button type="primary" @click="getTime">
              确定
            </el-button>
          </el-col>
        </el-form-item>

        <el-form-item class="time-list">
          <el-table :data="updateForm.imgInfo" border>
            <el-table-column type="index"
              :index="indexMethod"
              header-align=center>
            </el-table-column>
            <el-table-column
              prop="start"
              label="开始时间"
              width="150px"
              header-align=center
              :formatter="startCal"
              show-overflow-tooltip>
            </el-table-column>
          </el-table>
        </el-form-item>

        <el-form-item label="课程内容：" label-width="120px">
          <el-col :span="18">
            <el-input type="textarea"
              :autosize="{ minRows: 5, maxRows: 10}"
              auto-complete="true"
              placeholder="请输入内容"
              v-model="updateForm.courseContain"
              clearable
              required="required">
            </el-input>
          </el-col>
        </el-form-item>

        <el-form-item
          label=""
          label-width="120px"
          class="update-form-item">
          <el-col :span="18">
            <el-checkbox v-model="updateForm.messageOn">
              开放留言区
            </el-checkbox>
          </el-col>
        </el-form-item>

        <el-form-item
          label="价格："
          label-width="120px"
          class="update-form-input">
          <el-row width="300px">
            <el-input
              v-model="updateForm.price"
              auto-complete="true"
              required="required"
              width="100px">
            </el-input>
          </el-row>
        </el-form-item>

        <el-form-item label="赏金比例(0~1)："
          label-width="120px"
          class="update-form-input"
          v-if="updateForm.price!=0">
          <el-row width="300px">
            <el-input
              v-model="updateForm.balance"
              auto-complete="true"
              width="100px">
            </el-input>
          </el-row>
        </el-form-item>

        <el-form-item
          label="焚毁时间(小时)："
          label-width="120px"
          class="update-form-input">
          <el-row width="300px">
            <el-input
              v-model="updateForm.destroyTime"
              auto-complete="true"
              required="required"
              width="100px">
            </el-input>
          </el-row>
        </el-form-item>

        <el-form-item class="update-btn">
          <br />
          <el-button
            type="primary"
            @click="uploadcourse"
            icon="el-icon-upload">
            上传课程
          </el-button>
          <el-button
            icon="el-icon-delete"
            @click="clearpage"
            class="clear">
            清空
          </el-button>
          <br />
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
      updateForm: {
        courseId: NaN,
        courseTitle: '',
        courseDescription: '',
        timeList: [],
        courseContain: '',
        messageOn: true,
        price: 0,
        destroyTime: 0,
        audioId: NaN,
        audioList: [],
        imgList: [],
        imgInfo: [
          {
            id: '',
            start: '61'
          }
        ],
        percentage: 0
      },
      pictureIndex: -1,
      // uploadURL 为上传动作的后端接口
      dialogImageUrl: '',
      dialogVisible: false,
      input: '',
      dropdownMessage: '选择图片',
      miniteTemp: 0,
      secondeTemp: 0
    }
  },
  methods: {
    indexMethod: function(index) {
      return index + 1
    },
    startCal: function(data) {
      let minute = Math.floor(data.start / 60)
      let second = data.start - minute * 60
      return minute + '分' + second + '秒'
    },
    getTime: function() {
      let minite = 0
      let seconde = 0
      let secondes
      if (typeof this.pictureIndex === 'undefined') {
        this.$message({
          message: '请选择图片',
          type: 'warning'
        })
        return
      }
      try {
        if (this.miniteTemp) {
          minite = this.miniteTemp
        }
        if (this.secondeTemp) {
          seconde = this.secondeTemp
        }
        secondes = minite * 60 + seconde
        this.updateForm.imgInfo[this.pictureIndex].start = secondes
      } catch (err) {
        this.$message({
          message: '请输入正确时间',
          type: 'warning'
        })
      }
    },
    audioResponse: function(response) {
      this.updateForm.audioId = response.id
    },
    pictureResponse: function(response) {
      this.updateForm.imgInfo.push({id: response.id, start: 0})
    },
    upload_audio_URL: function() {
      return utils.getURL() + 'api/uploadaudio/'
    },
    upload_pic_URL: function() {
      return utils.getURL() + 'api/uploadcoursepicture/'
    },
    beforeUpload: function(file) {
      if (['audio/mp3', 'audio/wav'].indexOf(file.type) === -1) {
        this.$message.error('请上传正确的音频格式')
        return false
      }
    },
    handleChange: function(file, audioList) {
      this.audioList = audioList.slice(-1)
    },
    handleRemove: function(file, fileList) {
    },
    handlePictureCardPreview(file) {
      this.dialogImageUrl = file.url
      this.dialogVisible = true
    },
    clearpage: function() {
      this.updateForm.courseTitle = ''
      this.updateForm.courseDescription = ''
      this.updateForm.timeList = ''
      this.updateForm.courseContain = ''
      this.updateForm.messageRight = true
      this.updateForm.price = 0
      this.updateForm.destroyTime = 0
      this.updateForm.audioList = []
    },
    handleCommand: function(command) {
      this.pictureIndex = command - 1
      let time = this.updateForm.imgInfo[this.pictureIndex].start
      this.dropdownMessage = '图片' + command
      this.miniteTemp = Math.floor(time / 60)
      this.secondeTemp = time % 60
    },
    uploadcourse: function() {
      axios.post(utils.getURL() + 'api/uploadcourse/', qs.stringify({
        updateForm: JSON.stringify(this.updateForm)
      })).then(response => {
        if (response.data.status === 0) {
          this.$message({
            message: '创建成功',
            type: 'success'
          })
          location.replace()
        } else {
          this.$message.error('ERROR!')
        }
      })
    }
  },
  created: function() {
  }
}
</script>

<style scoped>
  .upload-page {
    text-align: center;
    position: absolute;
    margin: auto 5%;
    width: 70%;
  }
  .time-list {
    width: 200px;
    margin: 20px 120px;
  }
  .upload-inner {
    width: 100%;
    margin: 0 auto;
  }
  .el-form-item__content {
    text-align: left !important;
  }
  .time {
    color: black;
    font-size: 16px;
  }
  .upload-form {
    text-align: center;
  }
  .update-form-item {
    text-align: left;
  }
  .time-input {
     width: 80px;
  }
  .update-form-input {
    text-align: left;
    width: 250px;
  }
  .update-btn {
    text-align: right;
  }
</style>
