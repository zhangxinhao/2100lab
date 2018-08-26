import addAdmin from '@/components/admin/addAdmin'
import { mount } from '@vue/test-utils'

describe('addAdmin', () => {
  const wrapper = mount(addAdmin)
  it('有按钮', () => {
    expect(wrapper.contains('div')).toBe(true)
  })
  it('have a correct data', () => {
    expect(typeof addAdmin.data).toBe('function')
    const defaultData = addAdmin.data()
    expect(defaultData.newAdmin.courseManage).toBe(false)
  })
  it('click switchc', () => {
    wrapper.find('el-switch.change-c').trigger('click')
    const defaultData = addAdmin.data()
    expect(defaultData.newAdmin.courseManage).toBe(false)
  })
  it('click button', () => {
    wrapper.find('el-button.end').trigger('click')
  })
  it('click switcho', () => {
    wrapper.find('el-switch.change-o').trigger('click')
    const defaultData = addAdmin.data()
    expect(defaultData.newAdmin.orderManage).toBe(false)
    wrapper.vm.$nextTick(() => {
      expect(wrapper.vm.newAdmin.orderManage).toBe(true)
    })
  })
  it('click switch', () => {
    wrapper.find('el-input.inp').trigger('keydown.enter')
    wrapper.vm.$nextTick(() => {
      expect(wrapper.vm.response.data.status).toBe(0)
    })
  })
  it('渲染正确的标记', () => {
    expect(wrapper.html()).toContain('<el-form-item label="订单管理权限">')
  })
})
