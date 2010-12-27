<%inherit file="/base.mako" />

<%def name="head()">
${parent.head()}
<link rel="stylesheet" href="/css/style.css" type="text/css" />
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
<a href="/"><img src="/images/logo.png" alt="Andrea Ciofi" /></a>
</%def>



<div id="searchbar">
% if self.heading():
${self.heading()}
% endif
<span id="searchbar_right">
${h.form(h.url(controller='gallery', action='search'), method='GET')}
chose year: <a href="#">2010</a>
${h.text('searchterms', value='Search')}
${h.end_form()}
</span>
</div>

<%def name="heading()"></%def>

<div id="content">
${next.body()}
</div>
