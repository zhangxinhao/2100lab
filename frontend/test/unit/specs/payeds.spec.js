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
})
