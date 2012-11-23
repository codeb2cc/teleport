<!DOCTYPE html>
<html>
  <head>
    <title>Teleport - codeb2cc.com</title>
%include common/stylesheet.tpl debug=debug
  </head>
  <body>
%include common/header.tpl
    <div class="container main">
      <div class="row" style="margin-top: 100px;">
        <div class="span2"></div>
        <div class="span8">
          <div class="alert alert-block">
            <a href="/" class="close">x</a>
            <h4>{{ title }}</h4>
            {{ message }}
          </div>
        </div>
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
