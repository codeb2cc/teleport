;(function () {
  "use strict"
  $(function () {
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
  })
})()
