import baseAdmin from '@/components/admin/baseadmin'
import ElementUI from 'element-ui'
import Vue from 'vue'
Vue.use(ElementUI)

describe('baseAdmin', () => {
  it('correctlly logout', () => {
    const vm = new Vue(baseAdmin).$mount()
    vm.logout()
  })
  it('have a correct data', () => {
    expect(typeof baseAdmin.data).toBe('function')
    const defaultData = baseAdmin.data()
    expect(typeof defaultData.authorizationList).toBe('object')
  })
})
