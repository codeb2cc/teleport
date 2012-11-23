%if debug:
  <script src="/assets/js/lib/jquery/jquery-debug.js"></script>
  <script src="/assets/js/lib/bootstrap/bootstrap-debug.js"></script>
  <script src="/assets/js/lib/knockout/knockout-debug.js"></script>
%else:
  <script src="/assets/js/lib/jquery/jquery.js"></script>
  <script src="/assets/js/lib/bootstrap/bootstrap.js"></script>
  <script src="/assets/js/lib/knockout/knockout.js"></script>
  <script>

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

