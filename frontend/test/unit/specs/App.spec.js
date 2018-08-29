import App from '@/App'
import { mount } from '@vue/test-utils'
describe('App', () => {
  it('数目显示', () => {
    const wrapper = mount(App)
    let inputs = wrapper.findAll('div')
    expect(inputs.length).toBe(1)
  })
})
