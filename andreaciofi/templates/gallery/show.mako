<%inherit file="/layout.mako" />

<%def name="head()">
${parent.head()}
<script type="text/javascript" src="/js/lightbox.js"></script>
<script type="text/javascript">
<% lightbox_imgs = "[" %>
% for image in c.gallery.images:
    <% lightbox_imgs += h.literal('"') + h.image_url(image) + h.literal('",') %>
% endfor
<% lightbox_imgs = lightbox_imgs[:-1] + ']' %>
var lightbox_imgs = ${lightbox_imgs}
</script>
</%def>

<%def name="header()">
${parent.header()}
<div id="header_menu">
<a href="#"><img src="/images/about.png" alt="About" /></a><a href="/"><img src="/images/works.png" alt="Works" /></a>
</div>
</%def>

<%def name="heading()">${c.gallery.name.upper()}</%def>

<p>${h.process_text(c.gallery.text)}</p>
<p><b>Tags:
    % for tag in c.gallery.all_tags[:-1]:
        <a href="${h.url(controller='gallery', action='tag', tag=tag)}">
          ${tag}
        </a>,
    % endfor
    <a href="${h.url(controller='gallery', action='tag', tag=c.gallery.all_tags[-1])}">
      ${c.gallery.all_tags[-1]}
    </a>           
.</b>
</p>

<%
left = 0
middle = 0
right = 0
col_left = ""
col_right = ""
%>

% for video in c.gallery.videos:
    <%
    col_left += h.literal('<div class="gallery_video"><iframe src="http://player.vimeo.com/video/' + video + '" width="586" height="330" frameborder="0"></iframe></div>')
    left += 338
    middle += 338
    %>
% endfor

% for image in c.gallery.images:
% if left <= middle and left <= right:
    <%
    left += h.image_size(h.thumbnailer(image, max_width=289))[1] + 8
    col_left += h.literal('<a class="gallery_img_link" href="' + h.image_url(image) + '" target="_blank"><img src="' + h.thumbnailer_url(image, max_width=289) + '" class="gallery_img_left" /></a>')
    %>
% elif middle <= right:
    <%
    middle += h.image_size(h.thumbnailer(image, max_width=289))[1] + 8
    col_left += h.literal('<a class="gallery_img_link" href="' + h.image_url(image) + '" target="_blank"><img src="' + h.thumbnailer_url(image, max_width=289) + '" class="gallery_img_right" /></a>')
    %>
% else:
    <%
    right += h.image_size(h.thumbnailer(image, max_width=289))[1] + 8
    col_right += h.literal('<a class="gallery_img_link" href="' + h.image_url(image) + '" target="_blank"><img src="' + h.thumbnailer_url(image, max_width=289) + '" class="gallery_img_left" /></a>')
    %>
% endif
% endfor
<div class="gallery_imgs_left_col">${col_left}</div>
${col_right}
<hr/>
