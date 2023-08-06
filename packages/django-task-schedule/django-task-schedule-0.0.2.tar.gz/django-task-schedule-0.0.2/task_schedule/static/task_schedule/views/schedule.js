import {ColumnForm} from '../components/column-form.js'
import {TaskForm} from '../components/task-form.js'

export const Schedule = {
  props: ['permissions'],
  data() {
    return {
      header: [],
      grid: {},
      schedule: null,

      currentTime: [],
      hoverTime: [],

      columnForm: false,
      columnFormId: null,

      taskForm: false,
      taskFormId: null,
      taskFormColumn: null
    }
  },
  mounted() {
    this.updateSchedule()
  },
  methods: {
    updateSchedule() {
      this.$api('schedules/' + this.$route.params.id).then((response) => {
        this.schedule = response.data
        this.updateGrid()
      })
    },
    updateGrid() {
      let tzTime = this.getTzTime()

      // Init header and grid with time rows
      this.header = [{name: 'Time', colspan: 1}]
      this.grid = this.createTimeObj(Object)
      for (const [k, v] of Object.entries(this.grid)) {
        this.grid[k] = [
          {
            name: this.timeFormat(v.h, v.m),
            colspan: 1,
            rowspan: 1,
            refs: [],
            ref: 'time-' + k
          }
        ]
      }

      // Fill grid rows
      for (const c of this.schedule.data.columns) {
        let colRows = this.createTimeObj(Array)
        let topStart = 0
        for (const t of c.tasks) {
          const ref = 'task-' + t.id
          const start = t.hour * 60 + t.minute
          const end = start + t.duration
          let subColIndex = colRows[start].length
          for (let i = start; i < end; i += this.schedule.minute_step) {
            // Add ref to time
            this.grid[i][0].refs.push(ref)
            if (i === start) {
              // Add empty cells on top
              if (subColIndex) {
                for (let j = topStart; j < start; j += this.schedule.minute_step) {
                  if (colRows[j][subColIndex] === undefined) {
                    colRows[j][subColIndex] = null
                  }
                }
              } else {
                topStart = start
              }
              // Add start cell with task
              colRows[i][subColIndex] = {
                task: {
                  id: t.id,
                  name: t.name,
                  column: c,
                  rowspan: t.duration / this.schedule.minute_step,
                  k: i,
                  ref: ref
                },
                start: true
              }
            } else {
              // Add empty cell for task
              colRows[i][subColIndex] = {
                task: colRows[start][subColIndex].task,
                start: false
              }
            }
          }
        }

        // Calculate column base colspan and add column header
        const baseColspan = this.getBaseColspan(colRows)
        this.header.push({id: c.id, name: c.name, colspan: baseColspan})

        // Add column rows to grid
        for (const [k, row] of Object.entries(colRows)) {
          // If row is empty, fill it
          // with one base colspan cell.
          if (!row.length) {
            this.grid[k].push({
              name: '',
              column: c,
              colspan: baseColspan,
              rowspan: 1
            })
            continue
          }
          const colspan = baseColspan / row.length
          let rightSpans = 0
          for (const [_, cell] of row.entries()) {
            if (cell) {
              if (cell.start) {
                cell.task.colspan = colspan
                this.grid[k].push(cell.task)
                rightSpans += colspan
              } else {
                rightSpans += cell.task.colspan
              }
            } else {
              this.grid[k].push({
                name: '',
                colspan: colspan,
                rowspan: 1
              })
              rightSpans += colspan
            }
          }
          if (baseColspan - rightSpans) {
            this.grid[k].push({
              name: '',
              colspan: baseColspan - rightSpans,
              rowspan: 1
            })
          }
        }
      }

      // Add current time
      this.currentTime = this.grid[this.getTzTime()][0].refs
      this.grid[this.getTzTime()][0].now = true
    },
    // Param type is Array, Object or null
    createTimeObj(type) {
      const hours = Array.from(Array(24), (_, x) => x)
      const minutes = Array.from(
          Array(60 / this.schedule.minute_step), (_, x) => x * this.schedule.minute_step
      )
      const values = {}
      for (const h of hours) {
        for (const m of minutes) {
          if (type === Array) {
            values[h * 60 + m] = []
          } else if (type === Object) {
            values[h * 60 + m] = {h: h, m: m}
          } else {
            values[h * 60 + m] = null
          }
        }
      }
      return values
    },
    gcd(a, b) {
      return a ? this.gcd(b % a, a) : b
    },
    lcm(a, b) {
      return a * b / this.gcd(a, b)
    },
    getBaseColspan(colRows) {
      const values = new Set(Object.values(colRows).map((x) => x.length).filter((x) => x > 1))
      if (!values.size) {
        return 1
      }
      return Array.from(values).reduce(this.lcm)
    },
    timeFormat(h, m) {
      return h.toString().padStart(2, '0') + ':' + m.toString().padStart(2, '0')
    },
    getTzTime() {
      const d = new Date().toLocaleString('xx', {timeZone: this.schedule.tz})
      const h = parseInt(d.substr(12, 2))
      const m = Math.floor(parseInt(d.substr(15, 2)) / this.schedule.minute_step) * this.schedule.minute_step
      return h * 60 + m
    }
  },
  components: {
    ColumnForm,
    TaskForm
  },
  template: `
    <div v-if="schedule">
      <v-row>
        <v-col cols="1">
          <v-btn
            @click="$router.push({name: 'index'})"
            icon
            small
          ><v-icon>mdi-arrow-left</v-icon></v-btn>
        </v-col>
        <v-col cols="10">
          <h1 class="text-center">{{ schedule.name }}</h1>
        </v-col>
        <v-col cols="1"></v-col>
      </v-row>
      
      <v-simple-table
        v-if="grid && Object.keys(grid).length > 0"
        class="grid"
        dense
      >
        <thead>
          <tr>
            <th
              v-for="(item, index) in header"
              key="index"
              :colspan="item.colspan"
            >
              {{ item.name }}
              <v-btn
                v-if="item.id && permissions.has('change_column')"
                @click="columnFormId = item.id; columnForm = true"
                icon
                small
              ><v-icon>mdi-pencil</v-icon></v-btn>
              <v-btn
                v-if="item.id && permissions.has('add_task')"
                @click="taskFormColumn = item; taskFormId = null; taskForm = true"
                icon
                small
              ><v-icon>mdi-plus</v-icon></v-btn>
            </th>
            <th v-if="permissions.has('add_column')">
              Add column
              <v-btn
                @click="columnFormId = null; columnForm = true"
                icon
                small
              ><v-icon>mdi-plus</v-icon></v-btn>
            </th>
          </tr>
        </thead>
        
        <tbody>
          <tr v-for="(row, key) in grid" key="key">
            <td
              v-for="(item, index) in row"
              key="index"
              :colspan="item.colspan"
              :rowspan="item.rowspan"
              class="rounded-lg"
              :ref="item.ref"
              :class="{ task: !!item.name && index,
                        time: !index,
                        now: item.now || currentTime.indexOf(item.ref) != -1, 
                        hover: item.ref && hoverTime.indexOf(item.ref) != -1 }"
              @mouseover="hoverTime = item.refs ? item.refs.concat(item.ref): [item.ref]"
              @click="taskFormColumn = item.column; taskFormId = item.id; taskForm = taskFormColumn ? true : taskForm"
            >
              {{ item.name }}
            </td>
            
            <td v-if="permissions.has('add_column') && key == 0" :rowspan="Object.keys(grid).length"></td>
          </tr>    
        </tbody>
      </v-simple-table>
      
      <column-form
        v-model="columnForm"
        :permissions="permissions"
        :id="columnFormId"
        :schedule="schedule"
        @save="updateSchedule"
      ></column-form>
      
      <task-form
        v-model="taskForm"
        :permissions="permissions"
        :id="taskFormId"
        :schedule="schedule"
        :column="taskFormColumn"
        @save="updateSchedule"
      ></task-form>
    </div>
  `
}
