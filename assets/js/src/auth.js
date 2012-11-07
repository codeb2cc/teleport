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
          },
          error: function (jqXHR, textStatus, errorThrown) {
            console.warn('Invalid Email')
          }
        })
      }
      ko.computed(this.challenge, this)

      this.beforeSignIn = function () {
        if (!this.signIn.salt || !this.signIn.key()) {
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
