<%inherit file="/layout.mako"/>

<%def name="header()">
${parent.header()}
<span id="header_menu">
<a href="${h.url(controller='gallery', action='about')}"><img src="/images/aboutBlack.png" alt="About" /></a><a href="/"><img src="/images/works.png" alt="Works" /></a>
</span>
</%def>

<p>Andrea Ciofi degli Atti, architect</p>
<p>via della lungaretta 62, 00153 roma</p>
<p>telephone: 00390697658753, skype: andreaciofi</p>
