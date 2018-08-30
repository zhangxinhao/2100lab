import Vue from 'vue'
import Router from 'vue-router'
import store from '@/store.js'
import 'es6-promise/auto'
import axios from 'axios'
import * as utils from '@/components/utils/utils.js'

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

import adminLogin from '@/components/admin/adminLogin'
import baseAdmin from '@/components/admin/baseAdmin'
import addAdmin from '@/components/admin/addAdmin'
import orderAdmin from '@/components/admin/orderAdmin'
import uploadCourse from '@/components/admin/uploadCourse'
import courseManage from '@/components/admin/courseManage'
import commentAdmin from '@/components/admin/commentAdmin'
import userBrowsing from '@/components/admin/userBrowsing'
import userManage from '@/components/admin/userManage'
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
      path: '/adminLogin',
      name: 'adminLogin',
      component: adminLogin
    },
    {
      path: '/baseAdmin',
      name: 'baseAdmin',
      component: baseAdmin,
      children: [
        {
          path: '/addAdmin',
          component: addAdmin,
          name: 'addAdmin',
          beforeEnter: (to, from, next) => {
            if (store.state.userId === '0') {
              next('/adminLogin')
            } else {
              axios.post(utils.getURL() + 'api/accesscheck/').then(response => {
                let status = response.data.status
                let code = response.data.code
                if (status === 1) {
                  next('/adminLogin')
                } else {
                  if (code[0] === '1') {
                    next()
                  } else {
                    next(false)
                  }
                }
              })
            }
          }
        },
        {
          path: '/orderAdmin',
          component: orderAdmin,
          name: 'orderAdmin',
          beforeEnter: (to, from, next) => {
            if (store.state.userId === '0') {
              next('/adminLogin')
            } else {
              axios.post(utils.getURL() + 'api/accesscheck/').then(response => {
                let status = response.data.status
                let code = response.data.code
                if (status === 1) {
                  next('/adminLogin')
                } else {
                  if (code[4] === '1') {
                    next()
                  } else {
                    next(false)
                  }
                }
              })
            }
          }
        },
        {
          path: '/uploadCourse',
          name: 'uploadCourse',
          component: uploadCourse,
          beforeEnter: (to, from, next) => {
            if (store.state.userId === '0') {
              next('/adminLogin')
            } else {
              axios.post(utils.getURL() + 'api/accesscheck/').then(response => {
                let status = response.data.status
                let code = response.data.code
                if (status === 1) {
                  next('/adminLogin')
                } else {
                  if (code[1] === '1') {
                    next()
                  } else {
                    next(false)
                  }
                }
              })
            }
          }
        },
        {
          path: '/editCourse/:courseId',
          name: 'editCourse',
          component: uploadCourse,
          beforeEnter: (to, from, next) => {
            if (store.state.userId === '0') {
              next('/adminLogin')
            } else {
              axios.post(utils.getURL() + 'api/accesscheck/').then(response => {
                let status = response.data.status
                let code = response.data.code
                if (status === 1) {
                  next('/adminLogin')
                } else {
                  if (code[1] === '1') {
                    next()
                  } else {
                    next(false)
                  }
                }
              })
            }
          }
        },
        {
          path: '/courseManage',
          name: 'courseManage',
          component: courseManage,
          beforeEnter: (to, from, next) => {
            if (store.state.userId === '0') {
              next('/adminLogin')
            } else {
              axios.post(utils.getURL() + 'api/accesscheck/').then(response => {
                let status = response.data.status
                let code = response.data.code
                if (status === 1) {
                  next('/adminLogin')
                } else {
                  if (code[1] === '1') {
                    next()
                  } else {
                    next(false)
                  }
                }
              })
            }
          }
        },
        {
          path: '/commentAdmin',
          name: 'commentAdmin',
          component: commentAdmin,
          beforeEnter: (to, from, next) => {
            if (store.state.userId === '0') {
              next('/adminLogin')
            } else {
              axios.post(utils.getURL() + 'api/accesscheck/').then(response => {
                let status = response.data.status
                let code = response.data.code
                if (status === 1) {
                  next('/adminLogin')
                } else {
                  if (code[2] === '1') {
                    next()
                  } else {
                    next(false)
                  }
                }
              })
            }
          }
        },
        {
          path: '/userBrowsing',
          name: 'userBrowsing',
          component: userBrowsing,
          beforeEnter: (to, from, next) => {
            if (store.state.userId === '0') {
              next('/adminLogin')
            } else {
              axios.post(utils.getURL() + 'api/accesscheck/').then(response => {
                let status = response.data.status
                let code = response.data.code
                if (status === 1) {
                  next('/adminLogin')
                } else {
                  if (code[2] === '1') {
                    next()
                  } else {
                    next(false)
                  }
                }
              })
            }
          }
        },
        {
          path: '/userManage',
          name: 'userManage',
          component: userManage,
          beforeEnter: (to, from, next) => {
            if (store.state.userId === '0') {
              next('/adminLogin')
            } else {
              axios.post(utils.getURL() + 'api/accesscheck/').then(response => {
                let status = response.data.status
                let code = response.data.code
                if (status === 1) {
                  next('/adminLogin')
                } else {
                  if (code[2] === '1') {
                    next()
                  } else {
                    next(false)
                  }
                }
              })
            }
          }
        },
        {
          path: '/adminManage',
          component: adminManage,
          name: 'adminManage',
          beforeEnter: (to, from, next) => {
            if (store.state.userId === '0') {
              next('/adminLogin')
            } else {
              axios.post(utils.getURL() + 'api/accesscheck/').then(response => {
                let status = response.data.status
                let code = response.data.code
                if (status === 1) {
                  next('/adminLogin')
                } else {
                  if (code[0] === '1') {
                    next()
                  } else {
                    next(false)
                  }
                }
              })
            }
          }
        },
        {
          path: '/adminHistory',
          component: adminHistory,
          name: 'adminHistory',
          beforeEnter: (to, from, next) => {
            if (store.state.userId === '0') {
              next('/adminLogin')
            } else {
              axios.post(utils.getURL() + 'api/accesscheck/').then(response => {
                let status = response.data.status
                let code = response.data.code
                if (status === 1) {
                  next('/adminLogin')
                } else {
                  if (code[3] === '1') {
                    next()
                  } else {
                    next(false)
                  }
                }
              })
            }
          }
        },
        {
          path: '/dataAnalize',
          component: dataAnalize,
          name: 'dataAnalize',
          beforeEnter: (to, from, next) => {
            if (store.state.userId === '0') {
              next('/adminLogin')
            } else {
              axios.post(utils.getURL() + 'api/accesscheck/').then(response => {
                let status = response.data.status
                if (status === 1) {
                  next('/adminLogin')
                } else {
                  next()
                }
              })
            }
          }
        }
      ],
      beforeEnter: (to, from, next) => {
        if (store.state.userId === '0') {
          next('/adminLogin')
        } else {
          axios.post(utils.getURL() + 'api/accesscheck/').then(response => {
            let status = response.data.status
            if (status === 1) {
              next('/adminLogin')
            } else {
              next()
            }
          })
        }
      }
    }
  ]
})
