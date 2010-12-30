<%def name="images_delete_list(gallery)">
% for image in c.gallery.images:
    <table class="inlinetable">
      <tr><td>${h.checkbox('delete_image', value=image, checked=False)}</td></tr>
      <tr><td>
          <a href="${h.image_url(image)}" target="_blank">
            <img src="${h.thumbnailer_url(image, max_width=200, max_height=200)}" />
          </a></td></tr>
    </table>
% endfor
</%def>

${images_delete_list(c.gallery)}
