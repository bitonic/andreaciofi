<%inherit file="/layout.mako" />

<%def name="header()">
${parent.header()}
<div id="header_menu">
<a href="#"><img src="/images/about.png" alt="About" /></a><a href="/"><img src="/images/worksBlack.png" alt="Works" /></a>
</div>
</%def>

<%
left_col = 0
right_col = 0;
%>
% for gallery in c.galleries:
    <%
    thumb = h.thumbnailer(gallery.cover, max_width=438)
    if left_col <= right_col:
        left_col += h.image_size(thumb)[1]
        div_class = "gallery_entry_left"
    else:
        right_col += h.image_size(thumb)[1]
        div_class = "gallery_entry_right"
    %>
    <div class="${div_class}">
        <div class="gallery_entry_img">
            <a href="${h.url(controller='gallery', action='show', slug=gallery.slug)}">
                <img src="${h.image_url(thumb)}" alt="${gallery.name}" />
            </a>

            <div class="gallery_entry_tags">
                <a href="${h.url(controller='gallery', action='tag', tag=gallery.date.strftime('%Y'))}">
                    ${gallery.date.strftime('%Y')}
                </a>
                % if gallery.tags:
                    , 
                % endif
                % for tag in gallery.tags[:-1]:
                    <a href="${h.url(controller='gallery', action='tag', tag=tag)}">
                        ${tag}
                    </a>, 
                % endfor
                % if gallery.tags:
                <a href="${h.url(controller='gallery', action='tag', tag=gallery.tags[-1])}">
                    ${gallery.tags[-1]}
                </a> 
                % endif
            </div>
        </div>
        <div class="gallery_entry_name">
            <span class="gallery_entry_date">${gallery.date.strftime('%Y/%m')}</span> ${gallery.name}
        </div>
    </div>
% endfor

% if c.pages > 0:
    <div id="pages">
    % for p in range(1, c.pages + 1):
        % if p != c.page:
            <a href="${c.base_url + str(p)}">${p}</a>
        % else:
            ${p}
        % endif
    % endfor
    </div>
% endif
