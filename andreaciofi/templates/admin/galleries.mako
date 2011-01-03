<%inherit file="/admin/base.mako" />

<%def name="title()">${parent.title()} - Galleries</%def>

<%def name="heading()">Galleries</%def>

<% galleries = list(c.galleries) %>

<table id="galleries_table">
<tr>
    <th></th>
    <th>Date added</th>
    <th>Date</th>
    <th>Name</th>
    <th>Tags</th>
    <th>Text</th>
</tr>
% for gallery in galleries:
    <tr>
        <td>
	  % if gallery.cover:
        	  <img src="${h.thumbnailer_url(gallery.cover, max_width=200)}" />
	  % endif
	</td>
        <td>${gallery.created.strftime('%d-%m-%Y')}</td>
        <td>${gallery.date.strftime('%m-%Y')}</td>
        <td>${gallery.name}</td>
        <td>${", ".join(gallery.tags)}
        <td>${h.truncate_string(gallery.text)}</td>
        <td><a href="${h.url(controller='admin', action='edit_gallery', id=gallery.id)}">Edit</a></td>
        <td><a href="${h.url(controller='gallery', action='show', slug=gallery.slug)}" target="_blank">View</a></td>
    </tr>
% endfor
</table>
