import Vue from 'vue'
import Router from 'vue-router'
<<<<<<< HEAD
import HelloWorld from '@/components/HelloWorld'
=======
import index from '@/components/index'
>>>>>>> 0bf6f69539befa2f56645f29bd5a452dc36ec73b

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
<<<<<<< HEAD
      name: 'HelloWorld',
      component: HelloWorld
=======
      name: 'index',
      component: index
>>>>>>> 0bf6f69539befa2f56645f29bd5a452dc36ec73b
    }
  ]
})
