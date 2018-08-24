import orderAdmin from '@/components/admin/orderAdmin'
import ElementUI from 'element-ui'
import Vue from 'vue'
Vue.use(ElementUI)

describe('adminManage', () => {
  const vm = new Vue(orderAdmin).$mount()
  it('have correct flip', () => {
    vm.flipOver(2)
  })
})
