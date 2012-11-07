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
        <div class="alert">
          <a href="/" class="close">x</a>
          <strong>{{ message }}</strong>
        </div>
      </div>
    </div>
%include common/footer.tpl
  </body>
</html>
