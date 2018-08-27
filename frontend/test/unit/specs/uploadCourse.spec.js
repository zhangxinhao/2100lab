import uploadCourse from '@/components/admin/uploadCourse'
import ElementUI from 'element-ui'
import Vue from 'vue'
Vue.use(ElementUI)

describe('uploadCourse', () => {
  const vm = new Vue(uploadCourse).$mount()
  it('have correct audio url', () => {
    expect(vm.upload_audio_URL()).toBe('http://192.168.55.33:8000/api/uploadaudio/')
  })
  it('have correct pic url', () => {
    expect(vm.upload_pic_URL()).toBe('http://192.168.55.33:8000/api/uploadcoursepicture/')
  })
  it('correct before upload', () => {
    expect(vm.beforeUpload('1.mp4')).toBe(false)
  })
})
