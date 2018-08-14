import Vue from 'vue'
import Router from 'vue-router'
import index from '@/components/index'
import intro from '@/components/intro'
import coursepage from '@/components/coursepage'
import freelistpage from '@/components/freelistpage'

Vue.use(Router)

export default new Router({
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
    },
    {
      path: '/freelistpage',
      name: 'freelistpage',
      component: freelistpage
    }
  ]
})
