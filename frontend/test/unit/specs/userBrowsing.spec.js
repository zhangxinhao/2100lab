import userBrowsing from '@/components/admin/userBrowsing'
import { mount } from '@vue/test-utils'
import Vue from 'vue'
describe('userBrowsing', () => {
  const vm = new Vue(userBrowsing).$mount()
  it('翻页 ', () => {
    vm.flipOver(4)
    vm.$nextTick(() => {
      expect(vm._end).toBe(false)
    })
  })
  it('数目显示', () => {
    const wrapper = mount(userBrowsing)
    let inputs = wrapper.findAll('div')
    expect(inputs.length).toBe(6)
  })
})
