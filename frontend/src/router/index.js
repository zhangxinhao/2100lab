import Vue from 'vue'
import Router from 'vue-router'
import index from '@/components/index'
import intro from '@/components/intro'

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
    }
  ]
})
