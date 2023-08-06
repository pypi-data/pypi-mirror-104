import {Index} from './views/index.js'
import {Schedule} from './views/schedule.js'
import {PageNotFound} from './views/page-not-found.js'
import {Rules} from './components/rules.js'

Vue.use(VueRouter)

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

const router = new VueRouter({
  mode: 'history',
  routes: [
    {
      path: TASK_SCHEDULE_PREFIX,
      component: Index,
      name: 'index'
    }, {
      path: TASK_SCHEDULE_PREFIX + ':id',
      component: Schedule,
      name: 'schedule'
    }, {
      path: '*',
      name: '404',
      component: PageNotFound
    }
  ]
})

Vue.prototype.$api = axios.create({
  baseURL: TASK_SCHEDULE_PREFIX
})
Vue.prototype.$api.interceptors.response.use(
    (response) => response, (error) => alert(error)
)

Vue.prototype.$rules = Rules

new Vue({
  el: '#app',
  router,
  data() {
    return {
      permissions: null
    }
  },
  mounted() {
    this.$api.get('permissions').then((response) => {
      this.permissions = new Set(response.data)
    })
  },
  template: `
    <v-app>
      <v-main v-if="permissions">
        <v-container>          
          <v-row>
            <v-col cols="12">
              <router-view :permissions="permissions"></router-view>
            </v-col>  
          </v-row>
        </v-container>
      </v-main>
    </v-app>
  `,
  vuetify: new Vuetify()
})
