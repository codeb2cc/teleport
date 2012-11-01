<!DOCTYPE html>
<html>
  <head>
    <title>Teleport - codeb2cc.com</title>
    <link rel="stylesheet" href="/assets/css/bootstrap.css">
    <link rel="stylesheet" href="/assets/css/app.css">
    <script type="text/javascript" src="/assets/js/lib/jquery/jquery.js"></script>
    <script type="text/javascript" src="/assets/js/lib/knockout/knockout.js"></script>
    <script type="text/javascript" src="/assets/js/app.js"></script>
%if not debug:
    <script type="text/javascript">

      var _gaq = _gaq || [];
      _gaq.push(['_setAccount', 'UA-36025716-1']);
      _gaq.push(['_setDomainName', 'codeb2cc.com']);
      _gaq.push(['_trackPageview']);

      (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
      })();

    </script>
%end
  </head>
  <body>
    <header>
      <div class="container">
        <h2>Porject Teleport <small>% curl teleport.codeb2cc.com/ping</small></h2>
      </div>
    </header>
    <div class="container">
      <div class="row">
        <div class="span4">
          <dl>
            <dt>Username</dt>
            <dd id="info-username">Nobody</dd>
            <dt>Email</dt>
            <dd id="info-email">nobody@example.com</dd>
          </dl>
        </div>
        <div class="span8">
          <div>
            <div class="clearfix ib-wrap gate-control">
              <div class="ib" id="control-add">
                <div class="input-append">
                  <input type="text" data-bind="event: { keypress: $root.add }" placeholder="New gate..."></td>
                  <button type="button" class="btn" data-bind="click: $root.add, enable: gates().length < 5"><i class="icon-ok"></i></button>
                </div>
              </div>
              <div class="ib" id="control-search">
                <div class="input-append">
                  <input type="text" data-bind="event: { keyup: $root.search }" placeholder="Search ..."></td>
                  <button type="button" class="btn" data-bind="click: $root.search"><i class="icon-search"></i></button>
                </div>
              </div>
            </div>
          </div>
          <div>
            <!-- ko foreach: gates -->
            <div class="well gate-wrap" data-bind="fade: filterFlag">
              <div class="clearfix ib-wrap">
                <div class="ib gate-label" title="Gate Label">
                  <span class="icon"><i class="icon-tag"></i></span>
                  <div class="reader editable" data-bind="text: label, click: edit"></div>
                  <div class="input-append editor">
                    <input type="text" data-bind="value: label.peek(), event: { keypress: editLabel }">
                    <button type="button" class="btn" title="Edit" data-bind="click: editLabel"><i class="icon-edit"></i></button>
                    <button type="button" class="btn" title="Reset" data-bind="click: resetLabel"><i class="icon-refresh"></i></button>
                  </div>
                </div>
              </div>
              <div class="clearfix ib-wrap">
                <div class="ib gate-counter" title="Ping Counter">
                  <span class="icon"><i class="icon-map-marker"></i></span>
                  <div class="reader" data-bind="text: counter"></div>
                </div>
                <div class="ib gate-ip" title="Latest IP">
                  <span class="icon"><i class="icon-globe"></i></span>
                  <div class="reader" data-bind="text: ip"></div>
                </div>
              </div>
              <div class="clearfix ib-wrap">
                <div class="ib gate-description" title="Description">
                  <span class="icon"><i class="icon-comment"></i></span>
                  <div class="reader editable" data-bind="text: description, click: edit"></div>
                  <div class="input-append editor">
                    <input type="text" data-bind="value: description.peek(), event: { keypress: editDescription }">
                    <button type="button" class="btn" title="Edit" data-bind="click: editDescription"><i class="icon-edit"></i></button>
                    <button type="button" class="btn" title="Reset" data-bind="click: resetDescription"><i class="icon-refresh"></i></button>
                  </div>
                </div>
              </div>
              <div class="clearfix ib-wrap">
                <div class="ib gate-token" title="Ping Token">
                  <span class="icon"><i class="icon-barcode"></i></span>
                  <div class="reader"><span class="text-info" data-bind="text: token"></span></div>
                </div>
              </div>
              <div class="gate-action">
                <div class="btn-group">
                  <button type="button" class="btn" title="Reset Token" data-bind="click: $parent.reset"><i class="icon-repeat"></i></button>
                  <button type="button" class="btn" title="Delete Gate" data-bind="click: $parent.remove"><i class="icon-trash"></i></button>
                </div>
              </div>
            </div>
            <!-- /ko -->
          </div>
        </div>
      </div>
    </div>
  </body>
</html>
