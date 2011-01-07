<%inherit file="/layout.mako" />

<%namespace name="show_images" file="/gallery/show_images.mako"/>

<%def name="head()">
${parent.head()}
${show_images.javascript_list(c.galleries)}
</%def>

<%def name="header()">
${parent.header()}
<div id="header_menu">
<a href="#"><img src="/images/about.png" alt="About" /></a><a href="/"><img src="/images/worksBlack.png" alt="Works" /></a>
</div>
</%def>

<%def name="heading()">
ALL WORKS
% if c.tag:
    &middot; ${c.tag.upper()}
% endif
&middot;
% if c.tag:
    <a href="${h.url(controller='gallery', action='tag', tag=c.tag)}">VIEW PAGES</a>
% else:
    <a href="${h.url(controller='gallery', action='list')}">VIEW PAGES</a>
% endif
</%def>

${show_images.images_list(c.galleries)}
<hr/>
