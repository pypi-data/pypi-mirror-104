export const TaskForm = {
  props: ['value', 'id', 'schedule', 'column', 'permissions'],
  data() {
    return {
      value: false,
      name: '',
      hour: 0,
      minute: 0,
      duration: this.schedule.minute_step,
      confirmDelete: false
    }
  },
  mounted() {
  },
  computed: {
    selectHours() {
      return Array.from(Array(24), (_, x) => ({text: x, value: x}))
    },
    selectMinutes() {
      const values = []
      for (let i = 0; i <= 59; i += this.schedule.minute_step) {
        values.push({text: i, value: i})
      }
      return values
    },
    selectDurations() {
      const values = []
      for (let i = 0; i <= 1440; i += this.schedule.minute_step) {
        values.push({
          text: Math.floor(i / 60).toString().padStart(2, '0') + ':' + (i % 60).toString().padStart(2, '0'),
          value: i
        })
      }
      return values
    }
  },
  methods: {
    save() {
      if (!this.$refs.taskForm.validate()) {
        return
      }
      const data = {
        name: this.name,
        hour: parseInt(this.hour),
        minute: parseInt(this.minute),
        duration: parseInt(this.duration),
        column: this.column.id
      }
      if (this.id) {
        this.$api.put('tasks/' + this.id, data).then(() => {
          this.$emit('save')
          this.close()
        })
      } else {
        this.$api.post('tasks', data).then(() => {
          this.$emit('save')
          this.close()
        })
      }
    },
    del() {
      this.$api.delete('tasks/' + this.id).then(() => {
        this.$emit('save')
        this.close()
      })
    },
    close() {
      this.$emit('input', false)
    },
    validateDuration(value) {
      if (this.hour * 60 + this.minute + value > 1440) {
        return 'End of task time exceeds max value.'
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
        this.hour = 0
        this.minute = 0
        this.duration = this.schedule.minute_step
        this.confirmDelete = false
        this.$refs.taskForm.resetValidation()
        if (this.id) {
          this.$api.get('tasks/' + this.id).then(response => {
            this.name = response.data.name
            this.hour = response.data.hour
            this.minute = response.data.minute
            this.duration = response.data.duration
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
          <span class="headline">{{ id ? 'Edit' : 'Add' }} task</span>
        </v-card-title>
        <v-card-text>
          <v-form ref="taskForm" @submit.prevent="save">
            <v-container>
              <v-row>
                <v-col cols="12">
                  <v-text-field
                    label="Name*"
                    v-model="name"
                    :rules="[$rules.required, $rules.maxLength(255)]"
                    counter="255"
                    required
                  ></v-text-field>
                  <v-select
                    label="Hour*"
                    v-model="hour"
                    :items="selectHours"
                    required
                  ></v-select>
                  <v-select
                    label="Minute*"
                    v-model="minute"
                    :items="selectMinutes"
                    required
                  ></v-select>
                  <v-select
                    label="Duration*"
                    v-model="duration"
                    :items="selectDurations"
                    :rules="[validateDuration]"
                    required
                  ></v-select>
                </v-col>
              </v-row>
            </v-container>
          </v-form>
        </v-card-text>
        
        <v-card-actions>
          <div v-if="permissions.has('delete_task') && id">
            <v-btn
              v-if="!confirmDelete"
              color="red darken-1"
              text
              @click="confirmDelete = true"
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
