import { mount } from '@vue/test-utils'
import uploadCourse from '@/components/admin/uploadCourse'

describe('uploadCourse', () => {
  const wrapper = mount(uploadCourse)
  it('有输入框', () => {
    expect(wrapper.contains('el-input')).toBe(true)
  })
  it('have a correct data', () => {
    expect(typeof uploadCourse.data).toBe('function')
    const defaultData = uploadCourse.data()
    expect(defaultData.update_form.price).toBe(0)
  })
  it('click clear button', () => {
    wrapper.find('el-button.clear').trigger('click')
    const defaultData = uploadCourse.data()
    expect(defaultData.update_form.course_title).toBe('')
  })
})
