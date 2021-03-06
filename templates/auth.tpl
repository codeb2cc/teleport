<!DOCTYPE html>
<html>
  <head>
    <title>Teleport - codeb2cc.com</title>
%include common/stylesheet.tpl debug=debug
  </head>
  <body>
%include common/header.tpl
    <div class="container main">
      <div class="row" id="auth-form">
        <div class="span5">
          <div id="sign-mode">
            Sign <span class="active" data-bind="click: activeSignIn">IN</span>&nbsp;/&nbsp;<span data-bind="click: activeSignUp">UP</span>
          </div>
        </div>
        <div class="span7">
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
          <form class="form-horizontal" method="post" action="/signup/" id="form-sign-up" data-bind="submit: beforeSignUp" style="display: none;">
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
      <div class="row" id="auth-info">
        <div class="alert span6" data-bind="fade: alertMessage, text: alertMessage" style="display: none;"></div>
      </div>
    </div>
%include common/footer.tpl

%include common/script.tpl debug=debug
%if debug:
    <script src="/assets/js/auth-debug.js"></script>
%else:
    <script src="/assets/js/auth.js"></script>
%end
  </body>
</html>
