import baseadmin from '@/components/admin/baseadmin'
import ElementUI from 'element-ui'
import Vue from 'vue'
Vue.use(ElementUI)

describe('baseadmin', () => {
  it('correctlly logout', () => {
    const vm = new Vue(baseadmin).$mount()
    vm.logout()
  })
  it('have a correct data', () => {
    expect(typeof baseadmin.data).toBe('function')
    const defaultData = baseadmin.data()
    expect(typeof defaultData.authorizationList).toBe('object')
  })
})
