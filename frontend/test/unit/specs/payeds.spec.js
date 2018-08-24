import payeds from '@/components/user/payeds'
import { mount } from '@vue/test-utils'
import ElementUI from 'element-ui'
import Vue from 'vue'
Vue.use(ElementUI)

describe('payeds', () => {
  const wrapper = mount(payeds)
  it('登录按键与输入框', () => {
    let inputs = wrapper.findAll('el-table-column')
    expect(inputs.length).toBe(0)
  })
  it('数目显示', () => {
    let inputs = wrapper.findAll('span')
    expect(inputs.length).toBe(0)
    expect(wrapper.contains('el-dialog')).toBe(false)
  })
  const vm = new Vue(payeds).$mount()
  it('翻页 ', () => {
    vm.flipeOver(4)
    vm.$nextTick(() => {
      expect(vm._end).toBe(false)
    })
  })
})
