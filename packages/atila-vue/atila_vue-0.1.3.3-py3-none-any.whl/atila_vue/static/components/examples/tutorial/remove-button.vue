<template>
    <el-button @click='remove'>remove</el-button>
</template>


<script lang="babel">
  export default {
    props: {
      index: {type: Number, default: {}},
    },
    computed: {
      ...mapVuexItems (),
    },
    methods: {
        remove () {
            this.context.item_list [this.index].display = 'status-0'
        }
    }
  }
</script>
