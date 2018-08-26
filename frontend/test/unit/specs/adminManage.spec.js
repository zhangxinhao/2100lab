import adminManage from '@/components/admin/adminManage'
import ElementUI from 'element-ui'
import Vue from 'vue'
Vue.use(ElementUI)

describe('adminManage', () => {
  it('have correct data', () => {
    expect(typeof adminManage.data).toBe('function')
    const defaultData = adminManage.data()
    expect(defaultData.deleteIndex).toBe(0)
  })
  it('correctly sets the index', () => {
    const vm = new Vue(adminManage).$mount()
    expect(vm.indexMethod(4)).toBe(5)
  })
  it('correctly editFunction', () => {
    const vm = new Vue(adminManage).$mount()
    vm.editFunction(0)
    vm.$nextTick(() => {
      expect(vm.editVisible).toBe(true)
    })
  })
  it('correctly edit', () => {
    const vm = new Vue(adminManage).$mount()
    vm.edit()
    vm.$nextTick(() => {
      expect(vm.editVisible).toBe(false)
    })
  })
  it('correctly deleteFunction', () => {
    const vm = new Vue(adminManage).$mount()
    vm.deleteFunction(0)
    vm.$nextTick(() => {
      expect(vm.deleteVisible).toBe(true)
    })
  })
  it('correctly deleteIt', () => {
    const vm = new Vue(adminManage).$mount()
    vm.deleteIt()
    vm.$nextTick(() => {
      expect(vm.deleteVisible).toBe(false)
    })
  })
  let data = {courseManage: true, userManage: false, operationHistory: true, orderManage: true, adminManage: false}
  const vm = new Vue(adminManage).$mount()
  it('correctly courseRightCal', () => {
    expect(vm.courseRightCal(data)).toBe('开放')
  })
  it('correctly userRightCal', () => {
    expect(vm.userRightCal(data)).toBe('关闭')
  })
  it('correctly historyRightCal', () => {
    expect(vm.historyRightCal(data)).toBe('开放')
  })
  it('correctly orderRightCal', () => {
    expect(vm.orderRightCal(data)).toBe('开放')
  })
  it('correctly adminRightCal', () => {
    expect(vm.adminRightCal(data)).toBe('关闭')
  })
  it('correctly edit cancel', () => {
    vm.editCancel()
    vm.$nextTick(() => {
      expect(vm.editVisible).toBe(false)
    })
  })
  it('correctly delete cancel', () => {
    vm.deleteCancel()
    vm.$nextTick(() => {
      expect(vm.deleteVisible).toBe(false)
    })
  })
})
