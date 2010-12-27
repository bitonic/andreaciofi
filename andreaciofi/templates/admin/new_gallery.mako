<%inherit file="/admin/base.mako" />

<%def name="title()">${parent.title()} - Create new gallery</%def>

<%def name="heading()">Create new gallery</%def>

${h.form(h.url(controller='admin', action='do_edit_gallery'), method='POST', multipart=True)}
Name: ${h.text("name")}<br/>
Cover image: ${h.file("cover_image")}<br/>
Text: <br/>${h.textarea("text", cols=70, rows=8)}<br/>
Tags - separed by commas: ${h.text("tags")}<br/>
Date: ${h.select("year", h.datetime.now().strftime('%Y'), [str(y) for y in range(1980, h.datetime.now().year + 1)])}/${h.select("month", "1", [str(m) for m in range(1,13)])}<br/>
<h3>Images</h3>
Upload images - you can select multiple images:<br/>
<input name='images' type=file multiple />
<h3>Videos</h3>
<p>
Input the vimeo video id of the videos you want to add, separated by commas:<br/>
${h.text("videos", style='width:250px')}
</p>
${h.submit("submit", "Create gallery")}
${h.end_form()}
