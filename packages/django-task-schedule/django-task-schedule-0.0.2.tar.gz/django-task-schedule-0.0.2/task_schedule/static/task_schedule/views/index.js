import {ScheduleForm} from '../components/schedule-form.js'

export const Index = {
  props: ['permissions'],
  data() {
    return {
      schedules: null,
      scheduleForm: false,
      scheduleFormId: null
    }
  },
  methods: {
    updateSchedules() {
      this.$api.get('schedules').then(response => {
        this.schedules = response.data
      })
    }
  },
  mounted() {
    this.updateSchedules()
  },
  components: {
    ScheduleForm
  },
  template: `
    <div v-if="permissions && schedules">
      <h1 class="text-center">Task schedules</h1>
      
      <v-row>
        <v-col cols="3">
          <v-list>
            <v-list-item v-for="schedule in schedules" key="schedule.id">  
              <v-list-item-content>
                <v-list-item-title>
                  <router-link :to="{ name: 'schedule', params: {id: schedule.id} }">{{ schedule.name }}</a>
                </v-list-item-title>
              </v-list-item-content>
              <v-list-item-action>
                <v-btn
                  v-if="permissions.has('change_schedule')"
                  @click="scheduleFormId = schedule.id; scheduleForm = true"
                  icon
                ><v-icon>mdi-pencil</v-icon></v-btn>
              </v-list-item-action>
            </v-list-item>
            
            <v-list-item v-if="permissions.has('add_schedule')">
              <v-list-item-content>
                <v-list-item-title>
                  <a href="#" @click.prevent="scheduleFormId = null; scheduleForm = true"">Add schedule</a>
                </v-list-item-title>
              </v-list-item-content>
              <v-list-item-action>
                <v-btn @click="scheduleFormId = null; scheduleForm = true" icon>
                  <v-icon>mdi-plus</v-icon>
                </v-btn>
              </v-list-item-action>
            </v-list-item>
          </v-list>
        </v-col>
      </v-row>      

      <schedule-form
        v-model="scheduleForm"
        :permissions="permissions"
        :schedules="schedules"
        :id="scheduleFormId"
        @save="updateSchedules"
      ></schedule-form>
    </div>
  `
}
