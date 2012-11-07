<!DOCTYPE html>
<html>
  <head>
    <title>Teleport - codeb2cc.com</title>
%include common/stylesheet.tpl debug=debug
%include common/script.tpl debug=debug
%if debug:
    <script type="text/javascript" src="/assets/js/auth-debug.js"></script>
%else:
    <script type="text/javascript" src="/assets/js/auth.js"></script>
%end
  </head>
  <body>
%include common/header.tpl
    <div class="container main">
      <div class="row">
        <div class="span6">
          <div><span>Sign In</span></div>
          <form class="form-horizontal" method="post" action="/signin/" id="form-sign-in" data-bind="submit: beforeSignIn">
            <div style="display: hidden;">
              <input type="hidden" name="key" data-bind="value: signIn.key">
              <input type="hidden" name="password" data-bind="value: signIn.password">
            </div>
            <div class="control-group">
              <label class="control-label">Email</label>
              <div class="controls">
                <input type="text" name="email" placeholder="Email" data-bind="value: signIn.email">
              </div>
            </div>
            <div class="control-group">
              <label class="control-label">Password</label>
              <div class="controls">
                <input type="password" name="raw" placeholder="Password" data-bind="value: signIn.raw">
              </div>
            </div>
            <div class="control-group">
              <div class="controls">
                <button type="submit" class="btn">Sign in</button>
              </div>
            </div>
          </form>
        </div>
        <div class="span6">
          <div><span>Sign Up</span></div>
          <form class="form-horizontal" method="post" action="/signup/" id="form-sign-up" data-bind="submit: beforeSignUp">
            <div style="display: hidden;">
              <input type="hidden" name="key" data-bind="value: signUp.key">
              <input type="hidden" name="password" data-bind="value: signUp.password">
            </div>
            <div class="control-group">
              <label class="control-label">Email</label>
              <div class="controls">
                <input type="text" placeholder="Email" name="email" data-bind="value: signUp.email">
              </div>
            </div>
            <div class="control-group">
              <label class="control-label">Password</label>
              <div class="controls">
                <input type="password" placeholder="Password" name="raw" data-bind="value: signUp.raw">
              </div>
            </div>
            <div class="control-group">
              <label class="control-label">Confirm Password</label>
              <div class="controls">
                <input type="password" placeholder="Password Again" data-bind="value: signUp.confirm">
              </div>
            </div>
            <div class="control-group">
              <div class="controls">
                <button type="submit" class="btn">Sign up</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
%include common/footer.tpl
  </body>
</html>
