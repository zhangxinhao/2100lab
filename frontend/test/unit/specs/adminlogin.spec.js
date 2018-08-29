import adminLogin from '@/components/admin/adminlogin'
import ElementUI from 'element-ui'
import Vue from 'vue'
Vue.use(ElementUI)

describe('adminLogin', () => {
  const vm = new Vue(adminLogin).$mount()
  it('have correct data', () => {
    const defaultData = adminLogin.data()
    expect(defaultData.loForm.adminId).toBe('')
  })
  it('correctly login', () => {
    vm.login()
    vm.$nextTick(() => {
      expect(vm.status).toBe(0)
    })
  })
})
