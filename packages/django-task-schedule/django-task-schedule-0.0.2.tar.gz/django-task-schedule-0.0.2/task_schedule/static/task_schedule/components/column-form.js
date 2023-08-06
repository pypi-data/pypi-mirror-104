export const ColumnForm = {
  props: ['value', 'id', 'schedule', 'permissions'],
  data() {
    return {
      value: false,
      name: '',
      sort: 1000,
      tasks: [],
      confirmDelete: false
    }
  },
  mounted() {
  },
  methods: {
    save() {
      if (!this.$refs.columnForm.validate()) {
        return
      }
      const data = {name: this.name, sort: parseInt(this.sort), schedule: this.schedule.id}
      if (this.id) {
        this.$api.put('columns/' + this.id, data).then(() => {
          this.$emit('save')
          this.close()
        })
      } else {
        this.$api.post('columns', data).then(() => {
          this.$emit('save')
          this.close()
        })
      }
    },
    del() {
      this.$api.delete('columns/' + this.id).then(() => {
        this.$emit('save')
        this.close()
      })
    },
    close() {
      this.$emit('input', false)
    }
  },
  watch: {
    value() {
      if (!this.value) {
        return
      }
      this.$nextTick(() => {
        this.name = ''
        this.sort = 1000
        this.columns = []
        this.confirmDelete = false
        this.$refs.columnForm.resetValidation()
        if (this.id) {
          this.$api.get('columns/' + this.id).then(response => {
            this.name = response.data.name
            this.sort = response.data.sort
            this.tasks = response.data.data.tasks
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
          <span class="headline">{{ id ? 'Edit' : 'Add' }} column</span>
        </v-card-title>
        <v-card-text>
          <v-form ref="columnForm" @submit.prevent="save">
            <v-container>
              <v-row>
                <v-col cols="12">
                  <v-text-field
                    label="Name*"
                    v-model="name"
                    :rules="[$rules.required, $rules.maxLength(80)]"
                    counter="80"
                    required
                  ></v-text-field>
                  <v-text-field
                    label="Sort*"
                    v-model="sort"
                    :rules="[$rules.required, $rules.number(1,1000)]"
                    required
                  ></v-text-field>
                </v-col>
              </v-row>
            </v-container>
          </v-form>
        </v-card-text>
        
        <v-card-actions>
          <div v-if="permissions.has('delete_column') && id">
            <v-btn
              v-if="!confirmDelete"
              color="red darken-1"
              text
              @click="confirmDelete = true"
              :disabled="tasks.length > 0"
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
