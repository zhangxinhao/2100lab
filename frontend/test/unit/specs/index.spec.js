import userorder from '@/components/user/userorder'
import { mount } from '@vue/test-utils'
import ElementUI from 'element-ui'
import Vue from 'vue'
Vue.use(ElementUI)
describe('coursepage', () => {
  it('有按钮', () => {
    const wrapper = mount(userorder)
    expect(wrapper.contains('img')).toBe(false)
  })
})
