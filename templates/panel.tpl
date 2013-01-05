<!DOCTYPE html>
<html>
  <head>
    <title>Teleport - codeb2cc.com</title>
%include common/stylesheet.tpl debug=debug
  </head>
  <body>
%include common/header.tpl
    <div class="container main">
      <div class="row">
        <div class="span4">
          <div>
            <dl>
              <dt>Account <a href="/signout/" title="Sign out"><i class="icon-off"></i></a></dt>
              <dd>{{ user['email'] }}</dd>
            </dl>
          </div>
        </div>
        <div class="span8">
          <div>
            <p>Usage: <code>% curl teleport.codeb2cc.com/ping/?token=TOKEN [ &ip=IP ] [ &message=MESSAGE ]</code></p>
          </div>
          <div>
            <div class="clearfix ib-wrap gate-control">
              <div class="ib" id="control-add">
                <div class="input-append">
                  <input type="text" data-bind="event: { keypress: $root.add }" placeholder="New gate..."></td>
                  <button type="button" class="btn" data-bind="click: $root.add, enable: gates().length < 5"><i class="icon-plus"></i></button>
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
            <div class="well gate-wrap" data-bind="fade: hidden">
              <div class="clearfix ib-wrap">
                <div class="ib gate-label" title="Gate Label">
                  <span class="icon"><i class="icon-tag"></i></span>
                  <div class="reader editable" data-bind="text: label, click: edit"></div>
                  <div class="input-append editor">
                    <input type="text" data-bind="value: label.peek(), event: { keypress: $parent.edit }">
                    <button type="button" class="btn" title="Edit" data-bind="click: $parent.edit"><i class="icon-edit"></i></button>
                    <button type="button" class="btn" title="Reset" data-bind="click: reset"><i class="icon-refresh"></i></button>
                  </div>
                </div>
              </div>
              <div class="clearfix ib-wrap">
                <div class="ib gate-token" title="Ping Token">
                  <span class="icon"><i class="icon-barcode"></i></span>
                  <div class="reader"><span class="text-info" data-bind="text: token"></span></div>
                </div>
              </div>
              <div class="clearfix ib-wrap">
                <div class="ib gate-counter" title="Ping Counter">
                  <span class="icon"><i class="icon-list"></i></span>
                  <div class="reader" data-bind="text: counter"></div>
                </div>
                <div class="ib gate-ip" title="IP">
                  <span class="icon"><i class="icon-globe"></i></span>
                  <div class="reader" data-bind="text: ip"></div>
                </div>
              </div>
              <div class="clearfix ib-wrap">
                <div class="ib gate-message" title="Message">
                  <span class="icon"><i class="icon-comment"></i></span>
                  <div class="reader" data-bind="text: message"></div>
                </div>
              </div>
              <div class="gate-action">
                <div class="btn-group">
                  <button type="button" class="btn" title="Map" data-bind="click: $parent.map, enable: ip"><i class="icon-map-marker"></i></button>
                  <button type="button" class="btn" title="History" data-bind="click: $parent.history, enable: ip"><i class="icon-book"></i></button>
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
    <div class="modal hide fade" id="modal-map">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal">&times;</button>
        <h3>Location</h3>
      </div>
      <div class="modal-body">
        <div id="map-container"></div>
      </div>
    </div>
    <div class="modal hide fade" id="modal-history">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal">&times;</button>
        <h3>Ping History</h3>
      </div>
      <div class="modal-body" data-bind="with: activeGate">
        <table class="table table-hover">
          <thead>
            <tr>
              <th width="12">#</th>
              <th width="120">IP</th>
              <th>Message</th>
              <th width="160">Date</th>
            </tr>
          </thead>
          <tbody data-bind="foreach: records">
            <tr>
              <td data-bind="text: $index"></td>
              <td data-bind="text: ip"></td>
              <td data-bind="text: message"></td>
              <td>
                <div data-bind="text: date.toLocaleTimeString()"></div>
                <div data-bind="text: date.toLocaleDateString()"></div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn" data-dismiss="modal">Close</button>
      </div>
    </div>
%include common/footer.tpl

%include common/script.tpl debug=debug
%if debug:
    <script src="/assets/js/panel-debug.js"></script>
%else:
    <script src="/assets/js/panel.js"></script>
%end
  </body>
</html>
