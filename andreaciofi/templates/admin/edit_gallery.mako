<%inherit file="/admin/base.mako" />

<%def name="title()">${parent.title()} - Editing gallery</%def>

<%def name="heading()">Editing gallery "${c.gallery.name}"</%def>

${h.form(h.url(controller='admin', action='do_edit_gallery', id=c.gallery.id), method='POST')}
Name: ${h.text("name", value=c.gallery.name)}<br/>
Text: <br/>${h.textarea("text", cols=70, rows=8, content=c.gallery.text)}<br/>
Tags - separed by commas: ${h.text("tags", value=", ".join(c.gallery.tags))}<br/>
Date: ${h.select("year", h.datetime.now().strftime('%Y'), [str(y) for y in range(1980, h.datetime.now().year + 1)])}/${h.select("month", "1", [str(m) for m in range(1,13)])}<br/>
${h.submit("submit", "Edit gallery")}
${h.end_form()}
