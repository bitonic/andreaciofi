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
<span class="searchbar_right">
${h.form(h.url(controller='gallery', action='search'), method='GET')}
chose year:
<ul>
  <li><a href="${h.url(controller='gallery', action='tag', tag=c.years[0])}">${c.years[0]}</a>
    <ul>
    % for i in range(1, len(c.years)):
        <li><a href="${h.url(controller='gallery', action='tag', tag=c.years[i])}">${c.years[i]}</a></li>
    % endfor
    </ul>
  </li>
</ul>
${h.text('searchterms', value='Search')}
${h.end_form()}
</span>
</div>

<%def name="heading()"></%def>

<div id="content">
${next.body()}
</div>
