import Vue from 'vue'
import Vuex from 'vuex'
import 'es6-promise/auto'
import vuexAlong from 'vuex-along'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    userId: '0',
    courseId: '0'
  },
  mutations: {
    setUserId (state, userId) {
      state.userId = userId
    },
    setCourseId (state, courseId) {
      state.courseId = courseId
    }
  },
  plugins: [vuexAlong]
})

export default store
