<%inherit file="/admin/base.mako" />

<%def name="title()">${parent.title()} - Editing gallery</%def>

<%def name="heading()">Editing gallery "${c.gallery.name}"</%def>

${h.form(h.url(controller='admin', action='do_edit_gallery', id=c.gallery.id), method='POST', multipart=True)}
<p>
Name: ${h.text("name", value=c.gallery.name)}<br/>
<table><tr>
        <td>
	  % if c.gallery.cover:
              <img src="${h.thumbnailer_url(c.gallery.cover, max_width=300)}" /></td>
	  % endif
        <td>Change cover image:<br/>
          ${h.file("cover_image")}</td>
    </tr>
</table>
Text: <br/>${h.textarea("text", cols=70, rows=8, content=c.gallery.text)}<br/>
Tags - separed by commas: ${h.text("tags", value=", ".join(c.gallery.tags))}<br/>
Date: ${h.select("year", h.datetime.now().strftime('%Y'), [str(y) for y in range(1980, h.datetime.now().year + 1)])}/${h.select("month", "1", [str(m) for m in range(1,13)])}<br/>
</p>
<h3>Images</h3>
Upload images - you can select multiple images:<br/>
<input name='images' type=file multiple /><br/>
% if c.gallery.images:
    Check images to delete:<br/>
    % for image in c.gallery.images:
        <table class="inlinetable">
          <tr><td>${h.checkbox('delete_image', value=image, checked=False)}</td></tr>
          <tr><td>
              <a href="${h.image_url(image)}" target="_blank">
                <img src="${h.thumbnailer_url(image, max_width=200, max_height=200)}" />
              </a></td></tr>
        </table>
    % endfor
% endif
<h3>Videos</h3>
% if c.gallery.videos:
    Check the videos you want to delete:<br/>
    % for video in c.gallery.videos:
        <table class="inlinetable">
          <tr><td>${h.checkbox('delete_video', value=video, checked=False)}</td></tr>
          <tr>
            <td>
              <iframe src="http://player.vimeo.com/video/${video}" width="400" height="225" frameborder="0"></iframe>
            <td>
          </tr>
        </table>
    % endfor
% endif
<p>
Input the vimeo video id of the videos you want to add, separated by commas:<br/>
${h.text("videos", style='width:250px')}
</p>
${h.submit("submit", "Edit gallery")} -
<a href="${h.url(controller='admin', action='delete_gallery', id=c.gallery.id)}">Delete gallery</a>
${h.end_form()}
