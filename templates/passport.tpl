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
  </body>
</html>
