import commentadmin from '@/components/admin/commentadmin'
import ElementUI from 'element-ui'
import Vue from 'vue'
Vue.use(ElementUI)

describe('commentadmin', () => {
  const vm = new Vue(commentadmin).$mount()
  it('correctly ClearCourse', () => {
    vm.onSubmitClearCourse()
    vm.$nextTick(() => {
      expect(this.commentMsg.courseId).toBe('')
    })
  })
  it('correctly ClearPhone', () => {
    vm.onSubmitClearPhone()
    vm.$nextTick(() => {
      expect(this.commentMsg.phoneNumber).toBe('')
    })
  })
  it('correctly deleteMsg', () => {
    vm.deleteMsg(0)
    vm.$nextTick(() => {
      expect(vm.msgId).toBe(undefined)
    })
  })
  it('correctly forbidUser', () => {
    vm.forbidUser(0)
    vm.$nextTick(() => {
      expect(vm.userId).toBe(undefined)
    })
  })
})
