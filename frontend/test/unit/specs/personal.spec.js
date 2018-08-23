import personal from '@/components/user/personal'
import { mount } from '@vue/test-utils'

describe('personal', () => {
  it('有相关部件', () => {
    const wrapper = mount(personal)
    expect(wrapper.exists()).toBe(true)
  })
})
