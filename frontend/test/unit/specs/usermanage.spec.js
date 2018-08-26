import usermanage from '@/components/admin/usermanage'
import ElementUI from 'element-ui'
import Vue from 'vue'
Vue.use(ElementUI)

describe('usermanage', () => {
  const vm = new Vue(usermanage).$mount()
  it('correctly sets the index', () => {
    expect(vm.indexMethod(4)).toBe(5)
  })
  it('correctly deleteFunction', () => {
    vm.deleteFunction(0)
    vm.$nextTick(() => {
      expect(vm.deleteVisible).toBe(true)
    })
  })
  it('correct delete user', () => {
    vm.deleteUser()
    vm.$nextTick(() => {
      expect(vm.deleteVisible).toBe(false)
    })
  })
  it('correct forbideFunction', () => {
    vm.forbideFunction(1)
    vm.$nextTick(() => {
      expect(vm.forbideVisible).toBe(true)
    })
  })
  it('correct forbide user', () => {
    vm.forbideUser()
    vm.$nextTick(() => {
      expect(vm.forbideVisible).toBe(false)
    })
  })
  it('correct flipOver', () => {
    vm.flipOver(2)
  })
})
