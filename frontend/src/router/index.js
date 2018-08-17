import Vue from 'vue'
import Router from 'vue-router'

import index from '@/components/index'
import intro from '@/components/intro'
import coursepage from '@/components/coursepage'
import freelistpage from '@/components/freelistpage'
import personal from '@/components/personal'
import costlistpage from '@/components/costlistpage'
import brows from '@/components/brows'
import destroied from '@/components/destroied'
import payeds from '@/components/payeds'
import userorder from '@/components/userorder'
import personalinfor from '@/components/personalinfor'
import adminlogin from '@/components/admin/adminlogin'
import baseadmin from '@/components/admin/baseadmin'
import addAdmin from '@/components/admin/addAdmin'
import orderAdmin from '@/components/admin/orderAdmin'
import uploadCourse from '@/components/admin/uploadCourse'
import courseManage from '@/components/admin/courseManage'
import commentadmin from '@/components/admin/commentadmin'
import usermanage from '@/components/usermanage'
import userBrowsing from '@/components/admin/userBrowsing'

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
        },
        {
          path: '/userorder',
          component: userorder,
          name: userorder
        },
        {
          path: '/personalinfor',
          component: personalinfor,
          name: personalinfor
        }
      ]
    },
    {
      path: '/costlistpage',
      name: 'costlistpage',
      component: costlistpage
    },
    {
      path: '/destroied',
      name: 'destroied',
      component: destroied
    },
    {
      path: '/adminlogin',
      name: 'adminlogin',
      component: adminlogin
    },
    {
      path: '/baseadmin',
      name: 'baseadmin',
      component: baseadmin,
      children: [
        {
          path: '/addAdmin',
          component: addAdmin,
          name: addAdmin
        },
        {
          path: '/orderAdmin',
          component: orderAdmin,
          name: orderAdmin
        },
        {
          path: '/uploadCourse',
          name: 'uploadCourse',
          component: uploadCourse
        },
        {
          path: '/courseManage',
          name: 'courseManage',
          component: courseManage
        },
        {
          path: '/commentadmin',
          name: 'commentadmin',
          component: commentadmin
        },
        {
          path: '/userBrowsing',
          name: 'userBrowsing',
          component: userBrowsing
        }
      ]
    },
    {
      path: '/usermanage',
      name: 'usermanage',
      component: usermanage
    }
  ]
})
