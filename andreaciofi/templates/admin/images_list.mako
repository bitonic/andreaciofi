<%def name="images_delete_list(gallery)">
% for image in c.gallery.images:
    <table class="inlinetable">
      <tr><td><a href="javascript:delete_image('${h.url(controller='admin', action='delete_image', id=c.gallery.id, image=image)}')">X</a>
          <a href="${h.image_url(image)}" target="_blank">Fullsize</a></td></tr>
      <tr><td class="image_cell" id="${image}">
          <img src="${h.thumbnailer_url(image, max_width=200, max_height=200)}" />
      </td></tr>
    </table>
% endfor
</%def>

${images_delete_list(c.gallery)}
