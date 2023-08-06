<template>
  <article>
    <h1>ID: {{ id }}</h1>
    <h5>Index: #{{ index }}</h5>
    <h5>State sub types: {{ types }}</h5>
    <blockquote>{{ content }}</blockquote>
    <router-link :to="{ name: 'index'}">Go To Index</router-link>
    <br><br><br>
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
    data () {
      const arr = []
      for (let i = 0; i < 200; i++) {
        arr.push (i)
      }
      return {
        arr,
        id: this.$route.params.id,
        content: '',
      }
    },
    computed: {
      ...mapVuexItems (),
    },
    activated () {
      if (this.id != this.$route.params.id) {
        this.id = parseInt (this.$route.params.id)
        this.content = ''
        this.load ()
      }
    },
    mounted () {
      this.load ()
    },
    methods: {
      load () {
        setTimeout (() => {
          this.content = `Content ${ this.id } is loaded`
        }, 1000)
      }
    }
  }
</script>
