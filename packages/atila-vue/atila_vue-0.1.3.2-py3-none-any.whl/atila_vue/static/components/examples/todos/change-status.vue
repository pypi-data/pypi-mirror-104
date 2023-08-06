<template>
    <el-row>
      <el-col :xs=24 :sm=14 :md=12 :lg=10 :xl=2 class='px-3'>
        <div>
          <el-radio-group v-model="rows [rownum].status" :disabled="rows [rownum].status != 'todo'">
            <el-radio v-for="each, index in types" :label="each" :key='index' class="pr-0 mr-2" @change="v=>onChange (v)">
              {{ each.titleCase () }}</el-radio>
          </el-radio-group>
        </div>
      </el-col>

      <el-col :xs=24 :sm=10 :md=12 class="text-right">
        <el-button
          v-if="rows [rownum].status != 'todo'"
          @click="onChange ('todo')"
          type="danger" size:="small">TODO</el-button>
      </el-col>
    </el-row>
</template>

<script lang="babel">
  export default {
    props: {
      rownum: Number,
    },

    computed: {
      ...mapVuexItems (),
    },

    methods: {
      async onChange (val) {
        const old = this.rows [this.rownum].evaluated
        try {
          await axios.patch (this.$urlfor ('updateUrl', {id: this.rows [this.rownum].id}), { status: val })
          this.rows [this.rownum].status = val
        } catch (e) {
          this.$unotify ('API Failed, Reload and Retry Please', this.$traceback (e), 'error', 10000)
          this.rows [this.rownum].status = old
        }
      },
    },
  }
</script>
