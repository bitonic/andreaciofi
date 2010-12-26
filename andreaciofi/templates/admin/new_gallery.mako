<%inherit file="/admin/base.mako" />

<%def name="title()">${parent.title()} - Create new gallery</%def>

<%def name="heading()">Create new gallery</%def>

${h.form(h.url(controller='admin', action='do_edit_gallery'), method='POST')}
Name: ${h.text("name")}<br/>
Text: <br/>${h.textarea("text", cols=70, rows=8)}<br/>
Tags - separed by commas: ${h.text("tags")}<br/>
Date: ${h.select("year", h.datetime.now().strftime('%Y'), [str(y) for y in range(1980, h.datetime.now().year + 1)])}/${h.select("month", "1", [str(m) for m in range(1,13)])}<br/>
${h.submit("submit", "Create gallery")}
${h.end_form()}
