export const ScheduleForm = {
  props: ['value', 'schedules', 'id', 'permissions'],
  data() {
    return {
      value: false,
      name: '',
      minuteStep: 10,
      tz: 'UTC',
      selectTimezones: [],
      columns: [],
      confirmDelete: false
    }
  },
  mounted() {
    this.$api.options('schedules').then(response => {
      this.selectTimezones = response.data.actions.POST.tz.choices.map(x => ({text: x.display_name, value: x.value}))
    })
  },
  computed: {
    selectMinuteSteps() {
      return Array.from(Array(60), (_, x) => ({text: x + 1, value: x + 1})).filter(
          x => 60 % x.value === 0
      )
    }
  },
  methods: {
    save() {
      if (!this.$refs.scheduleForm.validate()) {
        return
      }
      const data = {
        name: this.name,
        minute_step: parseInt(this.minuteStep),
        tz: this.tz
      }
      if (this.id) {
        this.$api.put('schedules/' + this.id, data).then(() => {
          this.$emit('save')
          this.close()
        })
      } else {
        this.$api.post('schedules', data).then(() => {
          this.$emit('save')
          this.close()
        })
      }
    },
    del() {
      this.$api.delete('schedules/' + this.id).then(() => {
        this.$emit('save')
        this.close()
      })
    },
    close() {
      this.$emit('input', false)
    },
    validateName(value) {
      if (!this.schedules || !value) {
        return true
      }
      for (const [_, schedule] of this.schedules.entries()) {
        if (value.trim() === schedule.name && this.id !== schedule.id) {
          return 'Schedule with this name is already exists.'
        }
      }
      return true
    },
    validateMinuteStep(value) {
      for (const column of this.columns) {
        for (const task of column.tasks) {
          if (task.minute % value !== 0 || task.duration % value !== 0) {
            return 'Tasks fields are not multiples of the minute step.'
          }
        }
      }
      return true
    }
  },
  watch: {
    value() {
      if (!this.value) {
        return
      }
      this.$nextTick(() => {
        this.name = ''
        this.minuteStep = 10
        this.tz = 'UTC'
        this.columns = []
        this.confirmDelete = false
        this.$refs.scheduleForm.resetValidation()
        if (this.id) {
          this.$api.get('schedules/' + this.id).then(response => {
            this.name = response.data.name
            this.minuteStep = response.data.minute_step
            this.tz = response.data.tz
            this.columns = response.data.data.columns
          })
        }
      });
    }
  },
  template: `
    <v-dialog
      v-model="value"
      persistent
      max-width="600px"
      @click:outside="close"
      @keydown.esc="close"
      @keydown.enter="save"
    >
      <v-card>
        <v-card-title>
          <span class="headline">{{ id ? 'Edit' : 'Add' }} schedule</span>
        </v-card-title>
        <v-card-text>
          <v-form ref="scheduleForm" @submit.prevent="save">
            <v-container>
              <v-row>
                <v-col cols="12">
                  <v-text-field
                    label="Name*"
                    v-model="name"
                    :rules="[$rules.required, $rules.maxLength(80), validateName]"
                    counter="80"
                    required
                  ></v-text-field>
                  <v-select
                    label="Minute step*"
                    v-model="minuteStep"
                    :items="selectMinuteSteps"
                    :rules="[validateMinuteStep]"
                    required
                  ></v-select>
                  <v-select
                    label="Timezone*"
                    v-model="tz"
                    :items="selectTimezones"
                    required
                  ></v-select>
                </v-col>
              </v-row>
            </v-container>
          </v-form>
        </v-card-text>
        
        <v-card-actions>
          <div v-if="permissions.has('delete_schedule') && id">
            <v-btn
              v-if="!confirmDelete"
              color="red darken-1"
              text
              @click="confirmDelete = true"
              :disabled="columns.length > 0"
            >Delete</v-btn>
            <v-btn v-if="confirmDelete" color="red darken-1" text @click="del">Confirm delete</v-btn>
            <v-btn v-if="confirmDelete" color="blue darken-1" text @click="confirmDelete = false">Cancel</v-btn>
          </div>
          
          <v-spacer></v-spacer>
          
          <v-btn color="blue darken-1" text @click="close">Close</v-btn>
          <v-btn color="green darken-1" text @click="save">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  `
}
