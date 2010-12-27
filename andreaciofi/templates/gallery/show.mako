<%inherit file="/layout.mako" />

<%def name="header()">
${parent.header()}
<div id="header_menu">
<a href="#"><img src="/images/about.png" alt="About" /></a><a href="/"><img src="/images/works.png" alt="Works" /></a>
</div>
</%def>

<%def name="heading()">${c.gallery.name.upper()}</%def>

<p>${h.process_text(c.gallery.text)}</p>

<%
img_n = 0
images = len(c.gallery.images)
%>

% for video in c.gallery.videos:
<div class="gallery_video"><iframe src="http://player.vimeo.com/video/${video}" width="590" height="332" frameborder="0"></iframe></div>
% if img_n < images:
    <a href="${h.image_url(c.gallery.images[img_n])}" target="_blank">
      <img src="${h.thumbnailer_url(c.gallery.images[img_n], max_width=293, max_height=164, crop=True)}" class="gallery_img" />
    </a>
    <% img_n += 1 %>
% endif
% if img_n < images:
    <a href="${h.image_url(c.gallery.images[img_n])}" target="_blank">
      <img src="${h.thumbnailer_url(c.gallery.images[img_n], max_width=293, max_height=164, crop=True)}" class="gallery_img" />
    </a>
    <% img_n += 1 %>
% endif
% endfor

% for img_n in range(img_n, images):
    <a href="${h.image_url(c.gallery.images[img_n])}" target="_blank">
      <img src="${h.thumbnailer_url(c.gallery.images[img_n], max_width=293, max_height=164, crop=True)}" class="gallery_img" />
    </a>
% endfor

<hr/>
