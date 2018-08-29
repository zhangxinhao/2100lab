import dataAnalize from '@/components/admin/dataAnalize'
import { mount } from '@vue/test-utils'

describe('dataAnalize', () => {
  it('数目显示', () => {
    const wrapper = mount(dataAnalize)
    let inputs = wrapper.findAll('div')
    expect(inputs.length).toBe(7)
  })
})
