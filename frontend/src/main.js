// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import Share from 'vue-social-share'
import 'vue-social-share/dist/client.css'
import 'element-ui/lib/theme-chalk/display.css'
import './assets/iconfont/iconfont.css'

Vue.use(Share)
Vue.config.productionTip = false

Vue.use(ElementUI)
// Vue.use(Element, { size: 'small', zIndex: 3000 })

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App),
  components: { App },
  template: '<App/>'
})
