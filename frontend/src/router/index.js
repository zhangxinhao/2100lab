import Vue from 'vue'
import Router from 'vue-router'
import index from '@/components/index'
import intro from '@/components/intro'
import coursepage from '@/components/coursepage'
import freelistpage from '@/components/freelistpage'
import personal from '@/components/personal'
import costlistpage from '@/components/costlistpage'
import adminlogin from '@/components/adminlogin'
import brows from '@/components/brows'
import destroied from '@/components/destroied'
import payeds from '@/components/payeds'

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
    },
    {
      path: '/freelistpage',
      name: 'freelistpage',
      component: freelistpage
    },
    {
      path: '/personal',
      name: 'personal',
      component: personal,
      children: [
        {
          path: '/brows',
          component: brows,
          name: brows
        },
        {
          path: '/payeds',
          component: payeds,
          name: payeds
        }
      ]
    },
    {
      path: '/costlistpage',
      name: 'costlistpage',
      component: costlistpage
    },
    {
      path: '/adminlogin',
      name: 'adminlogin',
      component: adminlogin
    },
    {
      path: '/destroied',
      name: 'destroied',
      component: destroied
    }
  ]
})
