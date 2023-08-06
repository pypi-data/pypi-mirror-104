<template>
  <el-row type="flex" justify="center">
    <el-col :xs="16" :sm='12' :md='10' :lg="8" :xl="6">
        <el-button type="warning" @click="pushPermissionRequired"><span class="w-700">Confirn Web Push Notification</span></el-button>
    </el-col>
  </el-row>
</template>

<script lang="babel">
  export default {
    data () {
      return {
        messaging: null,
        tokenSent: false,
        swRegist: null,
      }
    },

    computed: {
      ...mapVuexItems (),
      config () {
        return this.context.frontendConfig
      },
    },

    mounted () {
      if ('serviceWorker' in navigator) {
        navigator.serviceWorker.ready.then ((regist) => {
          this.swRegist = regist
          this.$load_script ( [ this.config.firebaseScripts.appScriptUrl, this.config.firebaseScripts.messagingScriptUrl ], this.initFirebase)
        })
      }
    },

    methods: {
      initFirebase () {
          firebase.initializeApp(this.config.firebaseConfig)
          this.messaging = firebase.messaging()
          this.messaging.useServiceWorker (this.swRegist)
          this.messaging.usePublicVapidKey(this.config.webPush.certification)
          this.getToken ()
      },

      async pushPermissionRequired () {
        try {
          const permission = await Notification.requestPermission()
          if (permission === 'granted') {
            this.$log('notification permission granted.')
          } else {
            this.$log('unable to get permission to notify.')
          }
        } catch (error) {
          this.$traceback (error)
        }
      },

      async sendTokenToServer (token) {
        this.$log (`push token ${token}`)
        const resp = await this.$http.put ('/examples/webpush/tokens', {token: token})
        console.log (resp.data)
      },

      async getToken () {
        try {
          const currentToken = await this.messaging.getToken()
          if (currentToken) {
            this.sendTokenToServer(currentToken)
          } else {
            this.pushPermissionRequired()
            this.tokenSent = false
          }
        } catch (error) {
          this.$traceback (error)
          this.tokenSent = false
        }
      }
    },
  }
</script>
