<template>
  <div>
    <button @click='requestNotificationPermission' :class='isGranted ? "enabled":"disabled"'>{{ btnText }}</button>
    <button v-if='testButton' @click='testNotify'>Send Test Notification</button>
  </div>
</template>

<style scoped>
  .enabled {color: blue}
  .disabled {color: red}
</style>

<script lang="babel">
  export default {
    props: {
      testButton: Boolean,
      btnText: {
        type: String,
        default: 'Notification'
      },
    },
    data () {
      return {
        isGranted: Notification.permission === "granted",
      }
    },

    methods: {
      testNotify () {
        this.$nnotify ('HTTP-SFC', 'Created by Hans Roh', '/img/favicon/favicon-64.png')
      },

      requestNotificationPermission () {
        Notification.requestPermission().then((result) => {
            this.isGranted = result === 'granted'
        })
      },
    }
  }
</script>
