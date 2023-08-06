<template>
  <div>
    <button
      @click='handleSubscribe'
      :disabled='pushButtonDisabled || !swRegist'
      :class='isSubscribed ? "enabled":"disabled"'>{{ btnText }}</button>

    <div v-if='isSubscribed'>
      <div>{{ subscriptionMessage }}</div>
      <a  :href='pushCompanionLink'>{{ pushCompanionLink }}</a>
    </div>
  </div>
</template>

<style scoped>
  .enabled {color: blue}
  .disabled {color: red}
</style>

<script lang="babel">
  const pushCompanion = "https://web-push-codelab.glitch.me/"

  export default {
    props: {
      appServerPublicKey: {
        type: String,
        required: true
      },
      btnText: {
        type: String,
        default: 'Subscribe'
      },
      hideIfSubscribed: {
        type: Boolean,
        default: false
      },
    },

    data () {
      return {
        swRegist: false,
        isSubscribed: false,
        pushCompanionLink: pushCompanion,
        subscriptionMessage: '',
        pushButtonDisabled: true,
      }
    },

    beforeMount () {
      if ('serviceWorker' in navigator) {
        navigator.serviceWorker.ready.then ((regist) => {
          this.initPush (regist)
        })
      }
    },

    methods: {
      urlB64ToUint8Array (base64String) {
        const padding = '='.repeat((4 - base64String.length % 4) % 4)
        const base64 = (base64String + padding)
            .replace(/\-/g, '+')
            .replace(/_/g, '/')

        const rawData = window.atob(base64)
        const outputArray = new Uint8Array(rawData.length)

        for (let i = 0; i < rawData.length; ++i) {
            outputArray[i] = rawData.charCodeAt(i)
        }
        return outputArray
      },

      handleSubscribe () {
        if (this.isSubscribed) {
          this.unsubscribe ()
        } else {
          this.subscribe()
        }
      },

      updateSubscription (subscription) {
        if (Notification.permission === 'denied') {
          this.pushButtonDisabled = true
          subscription = null
        }
        else {
          this.pushButtonDisabled = false
        }

        if (subscription) {
          this.subscriptionMessage = JSON.stringify(subscription)
        } else {
          this.subscriptionMessage = ''
        }
      },

      unsubscribe () {
        this.swRegist.pushManager.getSubscription()
        .then(subscription => {
          if (subscription) {
            return subscription.unsubscribe();
          }
        })
        .catch(err => {
          this.$log(`Error unsubscribing ${ err }`)
        })
        .then(() => {
          this.updateSubscription(null)
          this.$unotify('Push Service', 'User is unsubscribed.')
          this.isSubscribed = false
        });
      },

      subscribe () {
        const applicationServerKey = this.urlB64ToUint8Array(this.appServerPublicKey);
        this.swRegist.pushManager.subscribe({
          userVisibleOnly: true,
          applicationServerKey: applicationServerKey
        })
        .then(subscription => {
          this.$unotify('Push Service', 'User is subscribed.')
          this.updateSubscription(subscription)
          this.isSubscribed = true
        })
        .catch(err => {
          this.$log (`Failed to subscribe the user: ${ err }`)
        })
      },

      initPush (swRegist) {
        this.swRegist = swRegist
        this.swRegist.pushManager.getSubscription()
        .then( (subscription) => {
          this.isSubscribed = !(subscription === null)
          this.updateSubscription(subscription)

          if (this.isSubscribed) {
            this.$log('User IS subscribed.')
          } else {
            this.$log('User is NOT subscribed.')
          }
        })
      }
    }
  }
</script>