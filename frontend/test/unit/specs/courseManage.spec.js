import courseManage from '@/components/admin/courseManage'
import ElementUI from 'element-ui'
import Vue from 'vue'
Vue.use(ElementUI)

describe('courseManage', () => {
  const vm = new Vue(courseManage).$mount()
  it('correctly sets the message when created', () => {
    expect(vm.indexMethod(2)).toBe(3)
  })
  it('correctly messageRightCal', () => {
    let data = {courseId: 15222, courseTitle: '我们爱科学', destroyTime: 8, messageRight: true, coursePrice: 25}
    expect(vm.messageRightCal(data)).toBe('开放')
  })
  it('correctly search', () => {
    vm.search()
  })
})
