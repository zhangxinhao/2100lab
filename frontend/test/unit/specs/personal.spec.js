import personal from '@/components/user/personal'
import { mount } from '@vue/test-utils'

describe('personal', () => {
  it('有相关部件', () => {
    const wrapper = mount(personal)
    expect(wrapper.exists()).toBe(true)
    let inputs = wrapper.findAll('span')
    expect(inputs.length).toBe(2)
    expect(wrapper.contains('el-dialog')).toBe(false)
  })
  it('数目显示', () => {
    const wrapper = mount(personal)
    let inputs = wrapper.findAll('div')
    expect(inputs.length).toBe(6)
  })
  it('数目显示', () => {
    const wrapper = mount(personal)
    let inputs = wrapper.findAll('table')
    expect(inputs.length).toBe(1)
  })
})
