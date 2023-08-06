<template>
  <el-row class="px-5 py-2 mb-6 lime lighten-4 elevation-1">
    <el-page-header @back="goBack" :content="context.siteName"></el-page-header>
  </el-row>
</template>

<script lang="babel">
  export default {
    computed: {
      ...mapVuexItems (),
    },

    methods: {
      goBack() {
        history.go (-1)
      },
    }
  }
</script>
