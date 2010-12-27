<%inherit file="/layout.mako" />

<%def name="header()">
${parent.header()}
<div id="header_menu">
<a href="#"><img src="/images/about.png" alt="About" /></a><a href="/"><img src="/images/works.png" alt="Works" /></a>
</div>
</%def>

<%def name="heading()">${c.gallery.name.upper()}</%def>

% for image in c.gallery.images:
    <a href="#"><img src="${h.thumbnailer_url(image, max_width=293, max_height=200, crop=True)}" class="gallery_img" /></a>
% endfor
