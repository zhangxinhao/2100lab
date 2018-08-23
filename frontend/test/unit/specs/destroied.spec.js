import destroied from '@/components/user/destroied'
import { mount } from '@vue/test-utils'
describe('destroied', () => {
  it('数目显示', () => {
    const wrapper = mount(destroied)
    let inputs = wrapper.findAll('div')
    expect(inputs.length).toBe(7)
  })
})
