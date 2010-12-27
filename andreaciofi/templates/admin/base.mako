<%inherit file="/base.mako" />

<%def name="head()">
${parent.head()}
<link rel="stylesheet" href="/css/admin.css" type="text/css" />
</%def>

<%def name="title()">Admin</%def>

<%def name="footer()">
<hr/>
<a href="${h.url(controller='admin', action='galleries')}">Galleries</a> - 
<a href="${h.url(controller='admin', action='new_gallery')}">Create new gallery</a>
</%def>

<h1>${next.heading()}</h1>

${next.body()}
