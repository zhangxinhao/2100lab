import addAdmin from '@/components/admin/addAdmin'
import { mount } from '@vue/test-utils'

describe('addAdmin', () => {
  it('有按钮', () => {
    const wrapper = mount(addAdmin)
    expect(wrapper.contains('div')).toBe(true)
  })
})
