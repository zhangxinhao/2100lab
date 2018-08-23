import adminHistory from '@/components/admin/adminHistory'
import ElementUI from 'element-ui'
import Vue from 'vue'
Vue.use(ElementUI)

describe('adminHistory', () => {
  it('correctly sets the message when created', () => {
    const vm = new Vue(adminHistory).$mount()
    expect(vm.indexMethod(5)).toBe(6)
  })
})
