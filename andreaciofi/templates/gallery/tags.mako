<%def name="tags(tags)">
% if tags:
    % for tag in tags[:-1]:
        <a href="${h.url(controller='gallery', action='tag', tag=tag)}">
          ${tag}
        </a>,
    % endfor
    <a href="${h.url(controller='gallery', action='tag', tag=tags[-1])}">
      ${tags[-1]}
    </a>.
% endif
</%def>
