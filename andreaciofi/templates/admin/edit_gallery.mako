<%inherit file="/admin/base.mako" />

<%def name="title()">${parent.title()} - Editing gallery</%def>

<%def name="heading()">Editing gallery "${c.gallery.name}"</%def>

${h.form(h.url(controller='admin', action='do_edit_gallery', id=c.gallery.id), method='POST')}
<p>
Name: ${h.text("name", value=c.gallery.name)}<br/>
Text: <br/>${h.textarea("text", cols=70, rows=8, content=c.gallery.text)}<br/>
Tags - separed by commas: ${h.text("tags", value=", ".join(c.gallery.tags))}<br/>
Date: ${h.select("year", h.datetime.now().strftime('%Y'), [str(y) for y in range(1980, h.datetime.now().year + 1)])}/${h.select("month", "1", [str(m) for m in range(1,13)])}<br/>
</p>
<h3>Videos</h3>
% if c.gallery.videos:
    Check the videos you want to delete:<br/>
    % for video in c.gallery.videos:
        <table class="video">
          <tr>
            <td>
              <iframe src="http://player.vimeo.com/video/${video}" width="400" height="225" frameborder="0"></iframe><td>
            <td>${h.checkbox('delete_video', value=video, checked=False)}</td>
          </tr>
        </table>
    % endfor
% endif
<p>
Input the vimeo video id of the videos you want to add, separated by commas:<br/>
${h.text("videos", style='width:250px')}
</p>
${h.submit("submit", "Edit gallery")}
${h.end_form()}
