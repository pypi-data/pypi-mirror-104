<template>
  <div class="pa-3 ml-0">
    <div>
      <b class="grey--text">Data Status </b>|
        <b class="ml-3">Record Count:</b> {{ count.format () }}
    </div>

    <div v-if='typeFilter' class="py-3">
      <b class="grey--text mr-5 hidden-xs-only">Type Filter |</b>
      <el-button-group class="text-xs-center text-sm-center">
        <a :href="$urlfor ('pagingUrl')"
          class="el-button el-button--mini"
          :class="!$args.type ? 'el-button--success':''">All</a>

        <a v-for="each, index in types" :href="$urlfor ('pagingUrl', {type: each})"
          :key="index"
          class="el-button el-button--mini"
          :class="each == $args.type ? 'el-button--success':''">{{ each.titleCase () }}</a>
      </el-button-group>
    </div>

  </div>
</template>

<script lang="babel">
  export default {
    props: {
      typeFilter: Boolean,
    },

    computed: {
      ...mapVuexItems (),
      count () {
        let matched = 0
        this.rows.forEach (row => {
          if (!this.$args.type || row.status == this.$args.type) {
            matched ++
          }
        })
        return this.context.record_count - this.rows.length + matched
      }
    }
  }
</script>
