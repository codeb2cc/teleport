;(function () {
  "use strict"

  $(function () {
    function AuthViewModel() {

      this.signIn = {
        salt: '',
        key: ko.observable(),
        password: ko.observable(),

        email: ko.observable(),
        raw: ko.observable()
      }

      this.signUp = {
        salt: '',
        key: ko.observable(),
        password: ko.observable(),

        email: ko.observable(),
        raw: ko.observable(),
        confirm: ko.observable()
      }

      this.alertMessage = ko.observable('')

      this.reset = function () {
        this.signIn.salt = ''
        this.signIn.key('')
        this.signIn.password('')
        this.signIn.email('')
        this.signIn.raw('')

        this.signUp.salt = ''
        this.signUp.key('')
        this.signUp.password('')
        this.signUp.email('')
        this.signUp.raw('')
        this.signUp.confirm('')

        this.alertMessage('')
      }

      this.challenge = function () {
        var that = this
        var email = this.signIn.email() || this.signUp.email()

        if (!email) { return false }

        $.ajax({
          url: '/challenge/',
          type: 'GET',
          data: { id: email },
          dataType: 'json',
          success: function (data, textStatus, jqXHR) {
            that.signIn.salt = data['code'][0]
            that.signIn.key(data['code'][1])
            that.signUp.salt = data['code'][0]
            that.signUp.key(data['code'][1])

            that.alertMessage('')
          },
          error: function (jqXHR, textStatus, errorThrown) {
            that.alertMessage('Invalid email')
          }
        })
      }
      ko.computed(this.challenge, this)

      this.activeSignIn = function (view, event) {
        $('#sign-mode span.active').removeClass('active')
        $(event.target).toggleClass('active')

        view.reset()

        $('#form-sign-up').hide()
        $('#form-sign-in').fadeIn()
      }

      this.activeSignUp = function (view, event) {
        $('#sign-mode span.active').removeClass('active')
        $(event.target).toggleClass('active')

        view.reset()

        $('#form-sign-in').hide()
        $('#form-sign-up').fadeIn()
      }

      this.beforeSignIn = function () {
        if (!this.signIn.salt || !this.signIn.key()) {
          this.alertMessage('User does not exist')

          return false
        }

        var hmac = window.SHA.hex_hmac_sha1(this.signIn.salt, this.signIn.raw())
        var nextHmac = window.SHA.hex_hmac_sha1(this.signIn.key(), this.signIn.raw())

        this.signIn.raw(hmac)
        this.signIn.password(nextHmac)

        return true
      }

      this.beforeSignUp = function () {
        if (!this.signUp.key()) {
          return false
        }

        if (this.signUp.raw().length < 6) {
          this.alertMessage('Password is too short (less than 6 characters)')

          return false
        } else if (this.signUp.raw() !== this.signUp.confirm()) {
          this.alertMessage('Passwords mismatch')

          return false
        }

        var hmac = window.SHA.hex_hmac_sha1(this.signUp.key(), this.signUp.raw())

        this.signUp.raw(hmac)
        this.signUp.confirm(hmac)
        this.signUp.password(hmac)

        return true
      }

    }

    var APP = new AuthViewModel()
    ko.applyBindings(APP)
  })

})()
