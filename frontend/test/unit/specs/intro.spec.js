import intro from '@/components/user/intro'
import { shallowMount, createLocalVue } from '@vue/test-utils'
import VueRouter from 'vue-router'

const localVue = createLocalVue()
localVue.use(VueRouter)
const router = new VueRouter()
shallowMount(intro, {
  localVue,
  router,
  stubs: ['router-link', 'router-view']
})

const $route = {
  path: '/:courseid',
  props: true,
  params: { courseid: '123' }
}
const wrapper = shallowMount(intro, {
  mocks: {
    $route
  }
})
describe('intro', () => {
  it('set a correct data', () => {
    expect(typeof intro.data).toBe('function')
    const defaultData = intro.data()
    expect(defaultData.title).toBe('我们爱科学')
  })

  it('有div', () => {
    expect(wrapper.contains('div')).toBe(true)
  })
  it('有弹框', () => {
    expect(wrapper.contains('el-dialog')).toBe(true)
  })
  it('有按钮', () => {
    expect(wrapper.contains('el-button')).toBe(true)
  })
})
