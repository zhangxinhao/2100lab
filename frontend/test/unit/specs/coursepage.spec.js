import Vue from 'vue'
import coursepage from '@/components/coursepage'

describe('coursepage.vue', () => {
  it('should render correct contents', () => {
    const Constructor = Vue.extend(coursepage)
    const vm = new Constructor().$mount()
    expect(vm.$el.querySelector('.user_ope').textContent)
      .toEqual('个人中心')
  })
})
