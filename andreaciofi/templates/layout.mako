<%inherit file="/base.mako" />

<%def name="head()">
${parent.head()}
<link rel="stylesheet" href="/css/style.css" type="text/css" />
<script type="text/javascript">
  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', '${c.analytics_id}']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();
</script>
</%def>

<%def name="title()">Andrea Ciofi</%def>

<%def name="footer()">
<a href="#" style="text-decoration: none;">&uarr; go to top</a> -
<script type="text/javascript">
emailE=('ma' + 'il@andreacio' + 'fi.c' + 'om')
document.write('<a href="mailto:' + emailE + '">' + 'contact' + '</a>')
</script>
<span class="footer_left">
  a website by <a href="mailto:e.imhotep@gmail.com">francesco mazzoli</a>, 2010
</span>
</%def>

<div id="header">
${self.header()}
</div>

<%def name="header()">
<a href="/" id="logo"><img src="/images/logo.png" alt="Andrea Ciofi" /></a>
</%def>



<div id="searchbar">
<span id="heading">
% if self.heading():
${self.heading()}
% endif
</span>
<span id="searchbar_right">
<!--${h.form(h.url(controller='gallery', action='search'), method='GET')}-->
choose year:
<ul>
  <li><a href="${h.url(controller='gallery', action='tag', tag=c.years[0])}">${c.years[0]}</a>
    <ul>
    % for i in range(1, len(c.years)):
        <li><a href="${h.url(controller='gallery', action='tag', tag=c.years[i])}">${c.years[i]}</a></li>
    % endfor
    </ul>
  </li>
</ul>
<!--${h.text('searchterms', value='Search')}-->
<!--${h.end_form()}-->
</span>
</div>

<%def name="heading()"></%def>

<div id="content">
${next.body()}
</div>
