<%inherit file="/admin/base.mako" />

<%namespace name="images_list" file="/admin/images_list.mako"/>

<%def name="title()">${parent.title()} - Editing gallery</%def>

<%def name="head()">
${parent.head()}
<script type="text/javascript" src="/fancyupload/source/Swiff.Uploader.js"></script>
<script type="text/javascript" src="/fancyupload/source/Fx.ProgressBar.js"></script>
<script type="text/javascript" src="/fancyupload/source/FancyUpload2.js"></script>
<script type="text/javascript">
var images_upload_url = '${url(controller='admin', action='upload_image', id=c.gallery.id)}';
var images_list_url = '${url(controller='admin', action='images_delete_list', id=c.gallery.id)}';
</script>
<script type="text/javascript" src="/js/photoqueue.js"></script>
<link rel="stylesheet" href="/css/photoqueue.css" type="text/css" />
</%def>

<%def name="heading()">Editing gallery "${c.gallery.name}"</%def>

${h.form(h.url(controller='admin', action='do_edit_gallery', id=c.gallery.id), method='POST', multipart=True, id='form-demo')}
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
Date: ${h.select("year", c.gallery.date.strftime('%Y'), [str(y) for y in range(1980, h.datetime.now().year + 1)])}/${h.select("month", str(int(c.gallery.date.strftime('%m'))), [str(m) for m in range(1,13)])}<br/>
</p>
<h3>Images</h3>
Upload images - you can select multiple images:<br/>
<div id="images_status" class="hide">
  <p>
    <a href="#" id="images_browse">Browse Files</a> |
    <a href="#" id="images_clear">Clear List</a> |
    <a href="#" id="images_upload">Start Upload</a>
    
  </p>
  <div>
    <strong class="overall-title"></strong><br />
    <img src="/fancyupload/assets/progress-bar/bar.gif" class="progress overall-progress" />
  </div>
  <div>
    <strong class="current-title"></strong><br />
    <img src="/fancyupload/assets/progress-bar/bar.gif" class="progress current-progress" />
  </div>
  
  <div class="current-text"></div>
</div>

<ul id="images_list"></ul><br/>
% if c.gallery.images:
    Check images to delete:<br/>
    <div id="images_delete_list">
      ${images_list.images_delete_list(c.gallery)}
    </div>
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
