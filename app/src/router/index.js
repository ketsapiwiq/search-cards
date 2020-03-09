import Vue from 'vue'
import Router from 'vue-router'
import LiveSearch from '@/components/LiveSearch'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'LiveSearch',
      component: LiveSearch
    }
  ]
})
