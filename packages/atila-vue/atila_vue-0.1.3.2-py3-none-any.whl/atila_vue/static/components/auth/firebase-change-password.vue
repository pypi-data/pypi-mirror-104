<template>
  <el-row type="flex" justify="center">
    <el-col class='sign-form'>
      <el-form :model="form" ref="form" :rules="rules" label-width="120px" size="small" label-position='top'>
        <div class='rd-2 sign-fields'>
          <h2 class='text-center'>Password Change</h2>
          <div class='text-left mb-6 blue-grey--text body-2'>
            Please enter your password twice, so we can verify you typed it in correctly.
          </div>

          <el-form-item prop="password" label="Password">
          <el-input type="password" v-model="form.password" clearable show-password></el-input>
          </el-form-item>

          <el-form-item prop="password_" label="Confirm Password">
          <el-input type="password" v-model="form.password_" clearable show-password></el-input>
          </el-form-item>

          <el-form-item class='text-center'>
          <el-button type="warning" @click="submitForm"><span class="w-700">Change Password</span></el-button>
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
        password: [
          { required: true, min: 8, max: 20, message: 'Length should be 8 to 20', trigger: ['blur', 'change'] },
        ],
        password_: [
          { required: true, validator: validatePassword, trigger: ['blur', 'change'] }
        ],
      }

      return {
        form: {
          password: '', password_: '',
        },
        rules
      }
    },

    computed: {
      ...mapVuexItems (),
      config () {
        return this.context.frontendConfig
      },
    },

    mounted () {
      this.$load_script ( [ this.config.firebaseScripts.appScriptUrl, this.config.firebaseScripts.authScriptUrl ], this.initFirebase)
    },

    methods: {
     goNext () {
      if (location.history) {
        location.history.back ()
      }
     },

     initFirebase () {
        firebase.initializeApp(this.config.firebaseConfig)
        this.reauthorize ()
     },

     async reauthorize () {
        const userProvidedPassword = await this.$uprompt (
            'Current Password',
            'Please enter your current password',
            /.{8,20}/,
            'Required 8-20 characters',
            'password'
        )

        if (!userProvidedPassword) {
            this.$ualert ('Password Change Canceled', 'You just canceled password change', this.goNext)
            return
        }
        this.$uloading (true, 'Authorizing...')
        const user = firebase.auth().currentUser
        const credential = firebase.auth.EmailAuthProvider.credential(
            user.email,
            userProvidedPassword
        )
        try {
            await user.reauthenticateWithCredential (credential)
            this.$uloading (false)
        } catch (error) {
            this.$uloading (false)
        }

      },

      // change password ---------------------------------
      async submitForm () {
        try {
          await this.$refs.form.validate ()
        } catch (e) {
          this.$unotify ('Invalid Form', 'Please review your inputs with red text', 'error')
          return
        }
        this.$uloading (true, 'Requesting...')
        try {
          await firebase.auth().currentUser.updatePassword (this.form.password)
          this.$ualert ('Password Changed', 'Your password has been updated successfully.', this.goNext)
        } catch (error) {
          this.$uloading (false)
          this.$unotify ('Changing Password Error', this.$traceback (error), 'error')
        }
      },

      resetForm () {
        this.$refs.form.resetFields ()
      },
    },
  }
</script>
