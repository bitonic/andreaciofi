<%def name="javascript_list(galleries)">
% if galleries:
<script type="text/javascript" src="/js/lightbox.js"></script>
<script type="text/javascript">
<% lightbox_imgs = "[" %>
% for gallery in galleries:
    % for image in gallery.images:
        <% lightbox_imgs += h.literal('"') + h.image_url(image) + h.literal('",') %>
    % endfor
% endfor
<% lightbox_imgs = lightbox_imgs[:-1] + ']' %>
var lightbox_imgs = ${lightbox_imgs};
</script>
% endif
</%def>

<%def name="images_list(galleries)">
<%
multiple = len(galleries) > 1
%>

% for gallery in galleries:
    <%
    left = 0
    middle = 0
    right = 0
    col_left = ""
    col_middle = ""
    col_right = ""
    %>

    % if multiple:
        <%
        link = h.literal('<div class="gallery_img_description"><a href="' + h.url(controller='gallery', action='show', slug=gallery.slug) + '"><span class="gallery_entry_date">' + gallery.date.strftime('%Y/%m') + '</span> ' + gallery.name + '</a></div>')
        right += 114 + 8
        col_right += link
        %>
    % endif
    <%
    for image in gallery.images:
        image_div =  h.literal('<a class="gallery_img_link" href="' + h.image_url(image) + '" target="_blank"><img src="' + h.thumbnailer_url(image, max_width=289) + '" class="gallery_img" /></a>')
        if left <= middle and left <= right:
            left += h.image_size(h.thumbnailer(image, max_width=289))[1] + 8
            col_left += image_div
        elif middle <= right:
            middle += h.image_size(h.thumbnailer(image, max_width=289))[1] + 8
            col_middle += image_div
        else:
            right += h.image_size(h.thumbnailer(image, max_width=289))[1] + 8
            col_right += image_div
    %>

    <div class="gallery_imgs">
      <div class="gallery_imgs_col_left">

      % for video in gallery.videos:
          <div class="gallery_video"><iframe src="http://player.vimeo.com/video/${video}" width="586" height="330" frameborder="0"></iframe></div>
          <%
          left += 338
          middle += 338
          %>
      % endfor

      <div class="gallery_imgs_col">${col_left}</div>
      <div class="gallery_imgs_col">${col_middle}</div>
      </div>
      <div class="gallery_imgs_col_right">${col_right}</div>
      <hr/>
    </div>
% endfor
</%def>
