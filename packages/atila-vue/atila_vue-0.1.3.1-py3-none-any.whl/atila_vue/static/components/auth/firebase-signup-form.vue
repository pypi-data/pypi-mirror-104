<template>
  <el-row type="flex" justify="center">
    <el-col class='sign-form'>
      <el-form :model="form" ref="form" :rules="rules" label-width="120px" size="small" label-position='top'>
        <div class='rd-2 sign-fields'>
          <h2 class='text-center'>Sign Up</h2>
          <div class='text-left mb-6 blue-grey--text body-2'>
            Please enter your email and password twice, so we can verify you typed it in correctly.
          </div>

          <el-form-item prop="displayName" label="Dispaly Name">
          <el-input v-model="form.displayName" clearable></el-input>
          </el-form-item>

          <el-form-item prop="email" label="Email">
          <el-input v-model="form.email" clearable></el-input>
          </el-form-item>

          <el-form-item prop="password" label="Password">
          <el-input type="password" v-model="form.password" clearable show-password></el-input>
          </el-form-item>

          <el-form-item prop="password_" label="Confirm Password">
          <el-input type="password" v-model="form.password_" clearable show-password></el-input>
          </el-form-item>

          <div class="mb-10">
            <el-checkbox v-model="agreement">I agree to the <a href="${this.context.frontendConfig.signIn.termsOfUseUrl}" target="_blank"><b>Terms of Use</b></a></el-checkbox>
          </div>

          <el-form-item class='text-center'>
          <el-button type="primary" @click="submitForm"><span class="w-700">Sign Up</span></el-button>
          <el-button type='danger' @click="goNext">Cancel</el-button>
          </el-form-item>

        </div>

      </el-form>
    </el-col>
  </el-row>
</template>

<script lang="babel">
  export default {
    data () {
      const validatePassword = (rule, value, callback) => {
        if (value !== this.form.password) callback (new Error ('Password does not match'))
        else callback ()
      }

      const rules = {
        email: [
          { required: true, message: 'Please input email address', trigger: 'blur' },
          { min: 6, max: 64, message: 'Length should be 6 to 64', trigger: ['blur', 'change'] },
          { type: 'email', message: 'Please input correct email address', trigger: ['blur', 'change'] },
        ],
        password: [
          { required: true, min: 8, max: 20, message: 'Length should be 8 to 20', trigger: ['blur', 'change'] },
        ],
        password_: [
          { required: true, validator: validatePassword, trigger: ['blur', 'change'] }
        ],
        displayName: [
          { required: true, min: 2, max: 40, message: 'Length should be 2 to 20', trigger: ['blur', 'change'] },
          { validator: this.validatedisplayName, trigger: ['blur', 'change'] }
        ],
      }

      return {
        form: {
          email: '', password: '', password_: '', displayName: ''
        },
        rules,
        provider_data: null,
        aborted: false,
        agreement: false
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
      this.$load_script ( [ this.config.firebaseScripts.appScriptUrl, this.config.firebaseScripts.authScriptUrl ], this.initFirebase)
    },

    methods: {
      async validatedisplayName (rule, value, callback) {
        try {
          const responseData = await this.$http.put(`/auth/nick_names/${this.form.displayName}`)
          return callback ()
        } catch (error) {
          return callback(new Error('This name is unavailable'))
        }
      },

      goNext () {
        location.href = this.context.nextUrl
      },

      initFirebase () {
        firebase.initializeApp(this.config.firebaseConfig)
        firebase.auth().onAuthStateChanged (async (user) => {
          if (user) {
            if (!this.form.email.length) {
              this.$uloading ()
              this.$ualert ('Already Signed In', 'You may be already signed in. Please sign out first.',this.goNext)
              return
            }
            try {
              if (this.form.displayName.length) {
                this.$uloading ('Updating Profile...')
                try {
                  await user.updateProfile ({displayName: this.form.displayName})
                } catch (error) {}
              }
              this.$uloading ('Authorizing...')
              this.provider_data = firebase.auth().currentUser.providerData[0]
              const idToken = await firebase.auth().currentUser.getIdToken(false)
              // console.log (this.provider_data)
              this.$emit ('signed-up', this.provider_data, {user, idToken})
            } catch (error) {
              this.$set_cloak (false)
              this.$uloading ()
              this.$unotify ('Sign Up Error', this.$traceback (error), 'error')
            }
          } else if (!this.aborted) {
            if (this.aborted) {
              this.$uloading ('Canceling...')
            } else {
              this.$set_cloak (false)
              this.$uloading ()
            }
          }
        })
      },

      async continueSignIn (payload) {
        const user = payload.user
        const idToken = payload.idToken
        if (!user.emailVerified && this.provider_data.email.indexOf ('__') != 0) {
          // only provider is 'password'
          this.$uloading ('Sending email for validation...')
          try { await user.sendEmailVerification () }
          catch (error) {}
        }
        try {
          const resp = await this.$http.post (this.$urlfor ('signInWithFirebaseIdToken'), {id_token: idToken})
          this.$uloading ()
          this.$ls.set ('access_token', resp.data.access_token)
          this.$ls.set ('refresh_token', resp.data.refresh_token)
          this.provider_data.isMember = resp.data.is_member
          this.$emit ('signed-in', this.provider_data)
        } catch (error) {
          this.$set_cloak (false)
          this.$uloading ()
          this.$unotify ('Sign Up Error', this.$traceback (error), 'error')
        }
      },

      // signin with eamil and password ---------------------------------
      async submitForm () {
        try {
          await this.$refs.form.validate ()
        } catch (e) {
          this.$unotify ('Invalid Form', 'Please review your inputs with red text', 'error')
          return
        }
        if (!this.agreement) {
          this.$unotify ('Terms Of Use', 'Please agree to the Terms of Use', 'error')
          return
        }
        this.$uloading ('Creating Account...')
        try {
          const result = await firebase.auth().createUserWithEmailAndPassword(this.form.email, this.form.password)
        } catch (error) {
          this.$uloading ()
          this.$unotify ('Sign Up Error', this.$traceback (error), 'error')
        }
      },

      resetForm () {
        this.$refs.form.resetFields ()
      },
    },
  }
</script>
