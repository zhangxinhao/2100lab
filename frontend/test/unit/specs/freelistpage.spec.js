import freelistpage from '@/components/user/freelistpage'
import Vue from 'vue'
describe('freelistpage', () => {
  const vm = new Vue(freelistpage).$mount()
  it('翻页 ', () => {
    vm.flipeOver(4)
    vm.$nextTick(() => {
      expect(vm._end).toBe(false)
    })
  })
})
