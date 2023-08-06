<template>
  <el-row type="flex" justify="center">
    <el-col class='sign-form'>
      <el-form :model="form" ref="form" :rules="rules" label-width="120px" size="small" label-position='top'>
        <div class='rd-2 sign-fields'>
          <h2 class='text-center'>Sign In</h2>
          <div class='text-left mb-6 blue-grey--text body-2'>
            Please enter your email and password. Or sign in with your social accounts.
          </div>

          <el-form-item prop="email" label="Email">
          <el-input v-model="form.email" clearable></el-input>
          </el-form-item>

          <el-form-item prop="password" label="Password">
          <el-input type="password" v-model="form.password" clearable show-password></el-input>
          </el-form-item>

          <el-form-item class='text-center'>
          <el-button type="primary" @click="submitForm"><span class="w-700">Sign In</span></el-button>
          <el-button @click="resetForm">Reset</el-button>
          <div class='mt-4'>
            <a href="#" @click='promptEmail ()'>Forgot Password?</a>
          </div>
          </el-form-item>

          <el-form-item label="Or Sign In with SNS Accounts" class='text-center btn-sns-signin'>
            <div v-if="providerActivated ('facebook')"><el-button @click='signInWithProvider ("facebook")' class='btn-signin w-700 indigo darken-2 white--text'><i class='fa fa-facebook pr-2 mr-2'></i>Sign In with Facebook</el-button></div>
            <div v-if="providerActivated ('google')"><el-button @click='signInWithProvider ("google")' class='btn-signin w-700 red darken-1 white--text'><i class='fa fa-google pr-2 mr-2'></i>Sign In with Google</el-button></div>
            <div v-if="providerActivated ('kakao')"><el-button @click='signInWith3rdParty ("kakao")' class='btn-signin w-700 yellow darken-2 black--text'><i class='fa fa-comment pr-2 mr-2 white--text'></i>Sign In with Kakao</el-button></div>
            <div v-if="providerActivated ('naver')"><el-button id="naver-id-signin" class='btn-signin w-700 ma-0 pa-0 black--text'></el-button></div>
          </el-form-item>

          <el-form-item class='text-center'>
            No SNS account? <a :href='$urlfor ("signUpForm", {return_url: $args.return_url})' class='ml-2 w-700'>Sign Up</a>
          </el-form-item>
        </div>

      </el-form>
    </el-col>
  </el-row>
</template>

<script lang="babel">

  export default {
    data () {
      const rules = {
      email: [
        { required: true, message: 'Please input email address', trigger: 'blur' },
        { min: 6, max: 64, message: 'Length should be 8 to 64', trigger: ['blur', 'change'] },
        { type: 'email', message: 'Please input correct email address', trigger: ['blur', 'change'] },
      ],
      password: [
        { required: true, min: 8, max: 20, message: 'Length should be 6 to 20', trigger: ['blur', 'change'] },
      ]
      }

      return {
        form: {
          email: '', password: ''
        },
        rules,
        provider_data: {},
        current_path: location.pathname,
        aborted: false,
        }
    },

    computed: {
      ...mapVuexItems (),
      config () {
        return this.context.frontendConfig
      },
    },

    mounted () {
      this.$uloading ('Checking Status...', 1.0)
      this.$load_script (
        [ this.config.firebaseScripts.appScriptUrl, this.config.firebaseScripts.authScriptUrl ],
        this.initFirebase
      )
      if (this.config.signIn.allowedProviders.naver) {
        this.$load_script (this.config.signIn.naver.scriptUrl, this.initNaver)
      }
    },

    methods: {
      // utils ---------------------------------------------
      isMobile () {
        return !(/(win16|win32|win64|mac|macintel)/i.test (navigator.platform))
      },

      providerActivated (provider) {
        return this.config.signIn.allowedProviders [provider]
      },

      makeRandomString (length) {
        let result = ''
        const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        for ( var i = 0; i < length; i++ ) {
            result += characters.charAt(Math.floor(Math.random() * characters.length))
        }
        return result
      },

      goNext () {
        location.href = this.context.nextUrl
      },

      // firebase 3rd party ---------------------------------------------
      signInith3rdParty (provider) {
        if (provider == 'kakao') {
          this.$load_script (this.config.signIn.kakao.scriptUrl, this.signInWithKakao)
        }
      },

      initNaver () {
        const redirectUrl = `${ location.protocol }//${ location.hostname}:${ location.port}` +  this.$urlfor ('signInForm', ['naver', this.context.nextUrl])
        const naverLogin = new naver.LoginWithNaverId({
          clientId: this.config.signIn.naver.clientId,
          callbackUrl: redirectUrl,
          isPopup: false,
          signInButton: { color:'green', type: 3, height: 32 },
          callbackHandle: false
        })
        naverLogin.init()
      },

      signInWithKakao () {
        Kakao.init(this.config.signIn.kakao.clientId)
        if (this.isMobile ()) {
          Kakao.Auth.login ({
            success: (resp) => {
              this.signInWithCustomToken ('kakao', resp.access_token)
            },
            fail: (error) => {
              this.$unotify ('Kakao Sign In Error', 'Please retry later', 'error')
            }
          })
        } else {
          const redirectUrl = `${ location.protocol }//${ location.hostname}:${ location.port}` +  this.$urlfor ('signInForm')
          Kakao.Auth.authorize ({
            redirectUri: redirectUrl,
            isPopup: false,
            state: `kakao:${ this.makeRandomString (8)}:${ this.context.nextUrl }`
          })
        }
      },

      async checkRedirected () {
        // get access token from 3rd party authorization code
        if (!this.$args.provider) {
          try {
            const result = await firebase.auth().getRedirectResult()
          } catch (error)   {
            this.$unotify ('Sign In Error', this.$traceback (error), 'error')
          }
          this.$set_cloak (false)
          this.$uloading ()
          return
        }
        this.context.nextUrl = this.$args.return_url

        if (this.$args.provider == 'naver') {
          let success = false
          for (let each of window.location.hash.substring (1).split ("&")) {
            if (each.indexOf ("access_token=") === 0) {
              this.signInWithCustomToken ('naver', each.substring (13))
              success = true
              break
            }
            if (!success) {
              this.$set_cloak (false)
              this.$uloading ()
              this.$unotify ('Naver Sign In Error', 'Please retry later', 'error')
            }
          }
        }

        else if (this.$args.provider == 'kakao') {
          this.$load_script (this.config.signIn.kakao.scriptUrl, () => {
            Kakao.init(this.config.signIn.kakao.clientId)
            const redirectUrl = `${ location.protocol }//${ location.hostname}:${ location.port}` +  this.$urlfor ('signInForm')
            Kakao.Auth.issueAccessToken ({
              redirectUri: redirectUrl,
              code: this.$args.code,
              success: (resp) => {
                this.signInWithCustomToken ('kakao', resp.access_token)
              },
              fail: (error) => {
                cosole.log (error)
                this.$set_cloak (false)
                this.$uloading ()
                this.$unotify ('Kakao Sign In Error', 'Please retry later', 'error')
              }
            })
          })
        }
      },

      // firebase -------------------------------------------
      initFirebase () {
        firebase.initializeApp(this.config.firebaseConfig)
        firebase.auth().onAuthStateChanged (async (user) => {
          if (user) {
            try {
              this.$uloading ('Authorizing...')
              if (this.provider_data.providerID === undefined && firebase.auth().currentUser.providerData.length) {
                this.provider_data = firebase.auth().currentUser.providerData[0]
              }
              const idToken = await firebase.auth().currentUser.getIdToken(false)
              try {
                const resp = await this.$http.get (this.$urlfor ('firebaseUsers', [user.uid]))
                this.continueSignIn ({user, idToken})
              } catch (error) {
                if (error.response.status == 404) {
                  this.$log ('new user detected')
                  this.$emit ('signed-up', this.provider_data, {user, idToken})
                } else {
                  throw error
                }
              }
            } catch (error) {
              this.$set_cloak (false)
              this.$uloading ()
              this.$unotify ('Sign In Error', this.$traceback (error), 'error')
            }
         } else if (!this.aborted) {
            if (this.aborted) {
              this.$uloading ('Canceling...')
            } else {
              this.checkRedirected ()
            }
          }
        })
      },

      async continueSignIn (payload) {
          try {
            const user = payload.user
            const idToken = payload.idToken
            const resp = await this.$http.post (this.$urlfor ('signInWithFirebaseIdToken'), {id_token: idToken})
            this.$ls.set ('access_token', resp.data.access_token)
            this.$ls.set ('refresh_token', resp.data.refresh_token)
            this.provider_data.isMember = resp.data.is_member
            this.$emit ('signed-in', this.provider_data)
          } catch (error) {
            this.$set_cloak (false)
            this.$uloading ()
            this.$unotify ('Sign In Error', this.$traceback (error), 'error')
          }
      },

      signInWithProvider (name) {
        let provider = null
        if (name == 'facebook') {
          provider = new firebase.auth.FacebookAuthProvider()
        } else if (name == 'google') {
          provider = new firebase.auth.GoogleAuthProvider()
          provider.addScope ('https://www.googleapis.com/auth/userinfo.email')
        }
        if (provider === null) {
          return this.$unotify ('Sign In Error', 'Unknown Authorization Provider', 'error')
        }
        firebase.auth().signInWithRedirect(provider)
      },

      async signInWithCustomToken (provider, access_token) {
        const payload = {
          provider: provider,
          access_token: access_token
        }
        try {
          const resp = await this.$http.post (this.$urlfor ('firebaseCustomToken'), payload)
          this.provider_data = resp.data.profile
          const custom_token = resp.data.custom_token
          const result = await firebase.auth().signInWithCustomToken (custom_token)
          if (!result.user.email && this.provider_data.email) {
            await firebase.auth().currentUser.updateEmail(this.provider_data.email)
          }
        } catch (error) {
          this.$set_cloak (false)
          this.$unotify ('Custom Token Sign In Error', this.$traceback (error), 'error')
        }
      },

      // signin with eamil and password ---------------------------------
      async submitForm () {
        try {
          await this.$refs.form.validate ()
        } catch (error) {
          this.$unotify ('Invalid Form', 'Please review your inputs with red text', 'error')
          return
        }

        this.$uloading ('Signing In...')
        try {
          const result = await firebase.auth().signInWithEmailAndPassword (this.form.email, this.form.password)
        } catch (error) {
          this.$uloading ()
          this.$unotify ('Sign In Error', this.$traceback (error), 'error')
        }
      },

      async promptEmail () {
        const emailAddress = await this.$uprompt (
          'Your Email', 'Please enter your registered email',
          /[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?/,
          'Invalid Email'
        )
        if (emailAddress) {
          try {
            await firebase.auth().sendPasswordResetEmail (emailAddress)
            this.$unotify ('Check Your Email', 'Password reset link has been sent', 'info')
          } catch (error) {
            this.$unotify ('Sending Email Failed', 'Please retry later', 'error')
          }
        }
      },

      resetForm () {
        this.$refs.form.resetFields ()
      },
    },
  }
</script>
