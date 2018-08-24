import brows from '@/components/user/brows'
import Vue from 'vue'
describe('brows', () => {
  const vm = new Vue(brows).$mount()
  it('翻页 ', () => {
    vm.flipeOver(4)
    vm.$nextTick(() => {
      expect(vm._end).toBe(false)
    })
  })
})
