import personalinfor from '@/components/user/personalinfor'
import Vue from 'vue'
describe('personalinfor', () => {
  const vm = new Vue(personalinfor).$mount()
  it('翻页 ', () => {
    vm.clickToChangeIcon()
    vm.$nextTick(() => {
      expect(vm.dialogVisible).toBe(false)
    })
  })
})
