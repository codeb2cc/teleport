// use strict;

ko.bindingHandlers['fade'] = {
  'update': function (element, valueAccessor) {
    var value = ko.utils.unwrapObservable(valueAccessor());
    var isCurrentlyVisible = !(element.style.display == "none");
    if (value && !isCurrentlyVisible)
      $(element).fadeIn()
    else if ((!value) && isCurrentlyVisible)
      $(element).fadeOut()
  }
}

$(function () {

  function Gate(data) {
    this.id = data.id
    this.label = ko.observable(data.label)
    this.counter = ko.observable(data.counter)
    this.token = ko.observable(data.token)

    $.each(data.records, function (index, record) {
      record['date'] = new Date(record['date'])
    })
    this.records = ko.observableArray(data.records)

    this.hidden = ko.observable(true)

    this.ip = ko.computed(function () {
      return this.records().length ? this.records()[0]['ip'] : ''
    }, this)

    this.message = ko.computed(function () {
      return this.records().length ? this.records()[0]['message'] : ''
    }, this)

    this.update = function (data) {
      this.id = data.id
      this.label(data.label)
      this.counter(data.counter)
      this.token(data.token)

      this.records.removeAll()
      for (var _i = 0; _i < data.records.length; _i++) {
        data.records[_i]['date'] = new Date(data.records[_i]['date'])
        this.records.push(data.records[_i])
      }
    }

    this.edit = function (gate, event) {
      var editor = $(event.target).next('.editor')

      editor.show()
      editor.find('input').focus()
    }

    this.reset = function (gate, event) {
      var editor = $(event.target).parents('.editor')

      editor.find('input').val(gate.label())
      editor.hide()
    }

  }

  function TeleportViewModel () {
    var that = this

    this.gates = ko.observableArray([])
    this.activeGate = ko.observable()

    // Topbar {
    this.add = function () {
      if (event.type === 'keypress' && event.keyCode !== 13) {
        return true
      }

      var jqInput = $('#control-add input')
      var newLabel = jqInput.val()

      if (this.gates().length >= 5 || newLabel === '') { return false }

      $.ajax({
        url: '/post/',
        type: 'POST',
        data: { label: newLabel },
        dataType: 'json',
        success: function (data, textStatus, jqXHR) {
          that.gates.unshift(new Gate(data['data']))
          jqInput.val('')
        },
        error: function (jqXHR, textStatus, errorThrown) {}
      })
    }

    this.search = function (v, e) {
      var jqInput = $('#control-search input')
      var searchStr = jqInput.val()

      $.each(this.gates(), function (index, gate) {
        gate.hidden((gate.label().search(searchStr) !== -1))
      })

      return true
    }

    // }

    // Gate action {
    this.edit = function (gate, event) {
      if (event.type === 'keypress' && event.keyCode !== 13) {
        return true
      }

      var editor = $(event.target).parents('.editor')

      $.ajax({
        url: '/put/',
        type: 'PUT',
        data: { id: gate.id, label: editor.find('input').val() },
        dataType: 'json',
        success: function (data, textStatus, jqXHR) {
          gate.update(data['data'])
          editor.hide()
        },
        error: function (jqXHR, textStatus, errorThrown) {}
      })
    }

    this.history = function (gate) {
      that.activeGate(null).activeGate(gate)
      $('#modal-history').modal('show')
    }

    this.reset = function (gate) {
      $.ajax({
        url: '/reset/',
        type: 'POST',
        data: { id: gate.id },
        dataType: 'json',
        success: function (data, textStatus, jqXHR) {
          gate.update(data['data'])
        },
        error: function (jqXHR, textStatus, errorThrown) {}
      })
    }

    this.remove = function (gate) {
      $.ajax({
        url: '/delete/',
        type: 'DELETE',
        data: { id: gate.id },
        dataType: 'json',
        success: function (data, textStatus, jqXHR) {
          that.gates.remove(gate)
        },
        error: function (jqXHR, textStatus, errorThrown) {}
      })
    }

    // }

    // Initial
    $.getJSON('/get/', function (data) {
      var mappedGates = $.map(data['data'], function (item) {
        return new Gate(item)
      })

      that.gates(mappedGates)
    })

  }

  var APP = new TeleportViewModel()
  ko.applyBindings(APP)
})
