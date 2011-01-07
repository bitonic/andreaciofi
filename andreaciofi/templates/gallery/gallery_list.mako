<%inherit file="/layout.mako" />

<%def name="header()">
${parent.header()}
<span id="header_menu">
<a href="#"><img src="/images/about.png" alt="About" /></a><a href="/"><img src="/images/worksBlack.png" alt="Works" /></a>
</span>
</%def>

<%def name="heading()">
% if c.pages > 1:
    % for p in range(1, c.pages + 1):
        % if p != c.page:
            <a href="${c.base_url + str(p)}">${p}</a>
        % else:
            <span style="font-weight:normal">${p}</span>
        % endif
    % endfor
    &middot;
% endif
% if hasattr(c, 'tag'):
    <a href="${h.url(controller='gallery', action='all_images', tag=c.tag)}">VIEW ALL</a>
% else:
    <a href="${h.url(controller='gallery', action='all_images')}">VIEW ALL</a>
% endif
</%def>

<%def name="gallery_entry(gallery, thumb)">
<div class="gallery_entry">
    <div class="gallery_entry_img">
        <a href="${h.url(controller='gallery', action='show', slug=gallery.slug)}">
            <img src="${h.image_url(thumb)}" alt="${gallery.name}" />
        </a>

        <div class="gallery_entry_tags">
          ${h.tags(gallery.all_tags)}
        </div>
    </div>
    <div class="gallery_entry_name">
        <span class="gallery_entry_date">${gallery.date.strftime('%Y/%m')}</span> ${gallery.name}
    </div>
</div>
</%def>

<%
left_col = 0
middle_col = 0
right_col = 0
left_col_entries = []
middle_col_entries = []
right_col_entries = []
%>

% for gallery in c.galleries:
    <%
    thumb = h.thumbnailer(gallery.cover, max_width=438)
    if left_col <= right_col and left <= right:
        left_col += h.image_size(thumb)[1] + 8
        left_col_entries.append(gallery)
    elif middle_col <= right_col:
        middle_col += h.image_size(thumb)[1] + 8
        middle_col_entries.append(gallery)
    else:
        right_col += h.image_size(thumb)[1] + 8
        right_col_entries.append(gallery)
    %>
% endfor

<div class="gallery_entries">
% for gallery in left_col_entries:
    ${gallery_entry(gallery, h.thumbnailer(gallery.cover, max_width=289))}
% endfor
</div>

<div class="gallery_entries">
% for gallery in middle_col_entries:
    ${gallery_entry(gallery, h.thumbnailer(gallery.cover, max_width=289))}
% endfor
</div>

<div class="gallery_entries">
% for gallery in right_col_entries:
    ${gallery_entry(gallery, h.thumbnailer(gallery.cover, max_width=289))}
% endfor
</div>

<div id="pages_bottom">
% if c.pages > 1:
    % for p in range(1, c.pages + 1):
        % if p != c.page:
            <a href="${c.base_url + str(p)}">${p}</a>
        % else:
            ${p}
        % endif
    % endfor
    &middot;
% endif
<a href="${h.url(controller='gallery', action='all_images')}">VIEW ALL</a>
</div>
