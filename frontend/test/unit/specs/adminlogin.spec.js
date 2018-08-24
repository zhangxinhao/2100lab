import adminlogin from '@/components/admin/adminlogin'
import ElementUI from 'element-ui'
import Vue from 'vue'
Vue.use(ElementUI)

describe('adminlogin', () => {
  const vm = new Vue(adminlogin).$mount()
  it('have correct data', () => {
    const defaultData = adminlogin.data()
    expect(defaultData.loform.adminId).toBe('')
  })
  it('correctly login', () => {
    vm.login()
    vm.$nextTick(() => {
      expect(vm.status).toBe(0)
    })
  })
})
