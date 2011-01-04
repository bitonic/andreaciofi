<%inherit file="/layout.mako" />

<%namespace name="show_images" file="/gallery/show_images.mako"/>

<%def name="head()">
${parent.head()}
${show_images.javascript_list([c.gallery])}
</%def>

<%def name="header()">
${parent.header()}
<div id="header_menu">
<a href="#"><img src="/images/about.png" alt="About" /></a><a href="/"><img src="/images/works.png" alt="Works" /></a>
</div>
</%def>

<%def name="heading()">${c.gallery.name.upper()}</%def>

% if c.gallery.text:
    ${h.process_text(c.gallery.text)}
% endif
<p><b>Tags:
    ${h.tags(c.gallery.all_tags)}
</b>
</p>

${show_images.images_list([c.gallery])}
<hr/>
