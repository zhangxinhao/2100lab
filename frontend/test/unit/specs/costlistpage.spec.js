import costlistpage from '@/components/user/costlistpage'
import Vue from 'vue'
describe('costlistpage', () => {
  const vm = new Vue(costlistpage).$mount()
  it('翻页 ', () => {
    vm.flipeOver(4)
    vm.$nextTick(() => {
      expect(vm._end).toBe(false)
    })
  })
})
