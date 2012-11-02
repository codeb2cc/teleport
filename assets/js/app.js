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
    this.description = ko.observable(data.description)
    this.counter = ko.observable(data.counter)
    this.token = ko.observable(data.token)

    $.each(data.records, function (index, record) {
      record['date'] = new Date(record['date'])
    })
    this.records = ko.observableArray(data.records)

    this.filterFlag = ko.observable(true)

    this.ip = ko.computed(function () {
      if (this.records().length) {
        return this.records()[0]['ip']
      }

      return ''
    }, this)

    this.edit = function (gate, event) {
      var editor = $(event.target).next('.editor')

      editor.show()
      editor.find('input').focus()
    }

    this.editLabel = function (gate, event) {
      if (event.type === 'keypress' && event.keyCode !== 13) {
        return true
      }

      var editor = $(event.target).parents('.editor')

      gate.label(editor.find('input').val())
      editor.hide()
    }

    this.resetLabel = function (gate, event) {
      var editor = $(event.target).parents('.editor')

      editor.find('input').val(gate.label())
      editor.hide()
    }

    this.editDescription = function (gate, event) {
      if (event.type === 'keypress' && event.keyCode !== 13) {
        return true
      }

      var editor = $(event.target).parents('.editor')

      gate.description(editor.find('input').val())
      editor.hide()
    }

    this.resetDescription = function (gate, event) {
      var editor = $(event.target).parents('.editor')

      editor.find('input').val(gate.description())
      editor.hide()
    }

  }

  function TeleportViewModel () {
    var that = this

    this.gates = ko.observableArray([])

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
        gate.filterFlag((gate.label().search(searchStr) !== -1))
      })

      return true
    }

    this.put = function (gate) {
      var _data = {
        id: gate.id,
        label: gate.label(),
        description: gate.description()
      }

      if (!Boolean(_data.id)) { return false }

      $.ajax({
        url: '/put/',
        type: 'PUT',
        data: _data,
        dataType: 'json',
        success: function (data, textStatus, jqXHR) {
          console.log('OK')
        },
        error: function (jqXHR, textStatus, errorThrown) {}
      })
    }

    this.remove = function (gate) {
      if (gate.id == null) {
        that.gates.remove(gate)

        return false
      }

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

    $.getJSON('/get/', function (data) {
      var mappedGates = $.map(data['data'], function (item) {
        return new Gate(item)
      })

      that.gates(mappedGates)

    })

  }

  ko.applyBindings(new TeleportViewModel())
})
