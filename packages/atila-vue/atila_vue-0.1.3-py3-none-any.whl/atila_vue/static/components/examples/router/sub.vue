<template>
  <article>
    <h1>#{{index}} sub types: {{ types }}</h1>
  </article>
</template>

<style scoped>
  article {
    color: #4904b3;
  }
</style>

<script lang="babel">
  export default {
    props: {
      index: {type: Number, default: 1},
    },
    computed: {
      ...mapVuexItems (),
    },
  }
</script>
