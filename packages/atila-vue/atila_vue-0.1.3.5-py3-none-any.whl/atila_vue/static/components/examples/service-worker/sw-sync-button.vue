<template>
  <button @click='registerSync'>{{ btnText }}</button>
</template>

<script lang="babel">

  export default {
    props: {
      tag: {
        type: String,
        required: true
      },
      btnText: {
        type: String,
        default: 'Sync'
      },
      fallbackFunction: {
        type: Function,
        default: () => {}
      },
    },

    data () {
      return {
        swRegist: null,
      }
    },

    computed: {
      ...mapVuexItems (),
    },

    methods: {
      register (swRegist) {
        this.swRegist = swRegist
        this.swRegist.sync.register (this.tag)
        this.$log (`sync registered: ${ this.tag }`)
      },

      registerSync () {
        if ('serviceWorker' in navigator && 'SyncManager' in window) {
          navigator.serviceWorker.ready.then ((regist) => {
            return this.register (regist)
          }).catch (() => {
            this.fallbackFunction ()
          })
        }
        else {
          this.fallbackFunction ()
        }
      },
    }
  }
</script>
