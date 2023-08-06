<template>
  <article class="pa-6">
    <h1>state.types: {{ types }}</h1>
    <component :is="kitten"></component>
    <inline-sub-component :index="2"></inline-sub-component>
    <sub-component :index="3"></sub-component>
    <ul>
      <li v-for='i in arr'><router-link :to="{ name: 'sub/:id', params: {id: i}}">item {{i}}</router-link></li>
    </ul>
  </article>
</template>

<style scoped>
  article {
    color: #4904b3;
  }

  #vuex-state li {
    word-break: break-all;
    word-wrap: break-word;
  }

</style>

<script lang="babel">
  export default  {
    data () {
      return {
        arr: []
      }
    },
    components: {
      'inline-sub-component': httpVueLoader ('/components/examples/router/sub.vue'),
    },
    computed: {
      ...mapVuexItems (),
      kitten () {
        return httpVueLoader ('/components/examples/router/sub.vue')
      }
    },
    methods: {
      ...websocketMethods (),
      handle_read (evt) {
        this.$log (`recv: ${ evt.data }`, 'websocket')
      },

      getCPUInfo () {
        this.$wspush ('cpu')
        setTimeout (this.getCPUInfo, 3000)
      }

    },
    mounted () {
      setTimeout (() => {
        for (let i = 0; i < 200; i++) {
            this.arr.push (i)
        }
      }, 3000)
      this.$wsconnect (`/examples/websocket?userid=hansroh`, this.handle_read)
      this.$wspush ('hello')
      this.getCPUInfo ()
    },
  }
</script>
