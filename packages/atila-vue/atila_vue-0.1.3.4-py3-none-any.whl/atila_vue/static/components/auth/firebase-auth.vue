<template>
  <div>
    <firebase-signup-form ref="form1" v-if="isSignup"
      @signed-up='(provider_data, payload) => {handleSignUp (provider_data, payload)}'
      @signed-in='(provider_data) => { handleSignIn (provider_data) }'></firebase-signup-form>
    <firebase-signin-form ref="form2" v-else
      @signed-up='(provider_data, payload) => {handleSignUp (provider_data, payload)}'
      @signed-in='(provider_data) => { handleSignIn (provider_data) }'></firebase-signin-form>
  </div>
</template>

<script lang="babel">
  export default {
    components: {
      'firebase-signin-form': httpVueLoader ('/components/auth/firebase-signin-form.vue'),
      'firebase-signup-form': httpVueLoader ('/components/auth/firebase-signup-form.vue'),
    },

    props: {
      isSignup: {
        type: Boolean,
        default: false
      },
      termsOfUseUrl: {
        type: String,
        default: '/'
      },
      profileEditUrl: {
        required: true,
        type: String
      },
      signUpHandler: {
        type: Function,
        default: null
      },
      signInHandler: {
        type: Function,
        default: null
      }
    },

    computed: {
      ...mapVuexItems (),
      currentForm () {
        return this.isSignup ? this.$refs.form1 : this.$refs.form2
      }
    },

    data () {
      return {
        debug: false,
        profile: {},
      }
    },

    mounted () {
      if (this.debug) {
        const payload = {
          displayName: null,
          //email: "hrroh1@sns.co.kr",
          phoneNumber: null,
          photoURL: null,
          providerId: "password",
          uid: "hrroh1@sns.co.kr",
        }
        this.handleSignIn (null, payload)
      }
    },

    methods: {
      async postProfile () {
        try {
          this.$uloading ('Updating...', 1.0)
          const resp = await this.$http.patch (this.$urlfor ('updateProfile', ['me']), this.profile)
        } catch (error) {}
        return null
      },

      async handleSignUp (provider_data, payload) {
        this.signUpHandler && this.signUpHandler (provider_data)
        this.currentForm.continueSignIn (payload)
      },

      async handleSignIn (provider_data) {
        if (!provider_data.isMember) {
          this.profile.maybe_nick_name = provider_data.displayName || ''
          this.profile.email = provider_data.email || null
        }
        this.profile.provider = provider_data.providerId || null
        this.profile.phone_no = provider_data.phoneNumber || null
        this.profile.photo_url = provider_data.photoURL || null
        this.profile.name = provider_data.name || null
        this.profile.gender = provider_data.gender || null
        this.profile.birthday = provider_data.birthday || null
        if (!!this.profile.gender) {
          this.profile.gender = this.profile.gender.substring (0,1).toUpperCase ()
        }
        await this.postProfile ()
        this.signInHandler && this.signInHandler (provider_data)
        this.currentForm.goNext ()
      },
    }
  }

/* provider_data examples
  <emailpass>
  displayName: null
  email: "a@b.co"
  phoneNumber: null
  photoURL: null
  providerId: "password"
  uid: "hrroh1@sns.co.kr"

  <google>
  displayName: "Hans Roh"
  email: null
  phoneNumber: null
  photoURL: "https://lh5.googleusercontent.com/-dbbnPbx1Ylg/AAAAAAAAAAI/AAAAAAAAAAA/ACHi3rc2wfLC9vWMyR_RAr9oegl1FvQUVg/photo.jpg"
  providerId: "google.com"
  uid: "7954664"

  <kakao>
  birthday: ""
  displayName: "Hans Roh"
  email: "a@b.co"
  gender: ""
  name: ""
  phoneNumber: ""
  photoURL: ""
  providerId: "kakao"
  uid: 128859
*/
</script>

