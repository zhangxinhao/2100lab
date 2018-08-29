import adminLogin from '@/components/admin/adminlogin'
import ElementUI from 'element-ui'
import { mount } from '@vue/test-utils'
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
  it('数目显示', () => {
    const wrapper = mount(adminLogin)
    let inputs = wrapper.findAll('h1')
    expect(inputs.length).toBe(1)
  })
})
