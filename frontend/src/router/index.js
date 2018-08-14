import Vue from 'vue'
import Router from 'vue-router'
import index from '@/components/index'
import intro from '@/components/intro'
import coursepage from '@/components/coursepage'

Vue.use(Router)

export default new Router({
  // mode: 'history',
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    },
    {
      path: '/intro',
      name: 'intro',
      component: intro
    },
    {
      path: '/coursepage',
      name: 'coursepage',
      component: coursepage
    }
  ]
})
