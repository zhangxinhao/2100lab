import uploadCourse from '@/components/admin/uploadCourse'
import { shallowMount, createLocalVue } from '@vue/test-utils'
import VueRouter from 'vue-router'

const localVue = createLocalVue()
localVue.use(VueRouter)
const router = new VueRouter()
shallowMount(uploadCourse, {
  localVue,
  router,
  stubs: ['router-link', 'router-view']
})
const $route = {
  path: '/:courseid',
  props: true,
  params: { courseid: '123' }
}
const wrapper = shallowMount(uploadCourse, {
  mocks: {
    $route
  }
})
describe('uploadCourse', () => {
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
