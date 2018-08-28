import Vue from 'vue'
import Router from 'vue-router'
import store from '@/store.js'
import 'es6-promise/auto'

import index from '@/components/user/index'
import intro from '@/components/user/intro'
import coursepage from '@/components/user/coursepage'
import freelistpage from '@/components/user/freelistpage'
import personal from '@/components/user/personal'
import costlistpage from '@/components/user/costlistpage'
import brows from '@/components/user/brows'
import destroied from '@/components/user/destroied'
import payeds from '@/components/user/payeds'
import userorder from '@/components/user/userorder'
import personalinfor from '@/components/user/personalinfor'

import adminlogin from '@/components/admin/adminlogin'
import baseadmin from '@/components/admin/baseadmin'
import addAdmin from '@/components/admin/addAdmin'
import orderAdmin from '@/components/admin/orderAdmin'
import uploadCourse from '@/components/admin/uploadCourse'
import courseManage from '@/components/admin/courseManage'
import commentadmin from '@/components/admin/commentadmin'
import userBrowsing from '@/components/admin/userBrowsing'
import usermanage from '@/components/admin/usermanage'
import adminManage from '@/components/admin/adminManage'
import adminHistory from '@/components/admin/adminHistory'
import dataAnalize from '@/components/admin/dataAnalize'

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
      path: '/intro/:courseid/:user',
      name: 'intro',
      component: intro,
      beforeRouteLeave(to, from, next) {
        if (to.name !== 'coursepage' && to.name !== 'intro') {
          store.commit('setCourseId', '0')
        }
        next()
      }
    },
    {
      path: '/coursepage/:courseid/:user',
      name: 'coursepage',
      component: coursepage,
      beforeEnter: (to, from, next) => {
        if (store.state.userId !== '0' && store.state.courseId !== '0') {
          next()
        } else {
          next(false)
        }
      },
      beforeRouteLeave(to, from, next) {
        if (to.name !== 'coursepage' && to.name !== 'intro') {
          store.commit('setCourseId', '0')
        }
        next()
      }
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
          name: 'brows'
        },
        {
          path: '/payeds',
          component: payeds,
          name: 'payeds'
        },
        {
          path: '/userorder',
          component: userorder,
          name: 'userorder'
        },
        {
          path: '/personalinfor',
          component: personalinfor,
          name: 'personalinfor'
        }
      ],
      beforeEnter: (to, from, next) => {
        const nextRoute = [
          'personal',
          'brows',
          'payeds',
          'useroder',
          'personalinfor'
        ]
        if (nextRoute.indexOf(to.name) >= 0) {
          if (store.state.userId !== '0') {
            next()
          } else {
            next('/')
          }
        } else {
          next('/')
        }
      }
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
          name: 'addAdmin'
        },
        {
          path: '/orderAdmin',
          component: orderAdmin,
          name: 'orderAdmin'
        },
        {
          path: '/uploadCourse',
          name: 'uploadCourse',
          component: uploadCourse
        },
        {
          path: '/editCourse/:courseId',
          name: 'editCourse',
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
        },
        {
          path: '/usermanage',
          name: 'usermanage',
          component: usermanage
        },
        {
          path: '/adminManage',
          component: adminManage,
          name: 'adminManage'
        },
        {
          path: '/adminHistory',
          component: adminHistory,
          name: 'adminHistory'
        },
        {
          path: '/dataAnalize',
          component: dataAnalize,
          name: 'dataAnalize'
        }
      ],
      beforeEnter: (to, from, next) => {
        const nextRoute = [
          'baseadmin', 'addAdmin', 'orderAdmin',
          'uploadCourse', 'editCourse', 'courseManage',
          'commentadmin', 'userBrowsing', 'usermanage',
          'adminManage', 'adminHistory', 'dataAnalize'
        ]
        const list = [
          ['addAdmin', 'adminManage'],
          ['uploadCourse', 'editCourse', 'courseManage'],
          ['usermanage', 'userBrowsing', 'commentadmin'],
          ['adminHistory'],
          ['orderAdmin']
        ]
        if (nextRoute.indexOf(to.name) >= 0) {
          if (store.state.userId !== '0') {
            list[5] = []
            next()
          } else {
            next('/adminlogin')
          }
        } else {
          next('/adminlogin')
        }
      }
    }
  ]
})
