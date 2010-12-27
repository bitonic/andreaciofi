## -*- coding: utf-8 -*-
<!DOCTYPE html>
<!--<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">-->
<html>
<head>
    <title>${self.title()}</title>
    ${self.head()}
</head>
<body>
<div id="wrapper">
    <% flashes = h.flash.pop_messages() %>
    % if flashes:
        % for flash in flashes:
            <div id="flash">
                <span class="message">${flash}</span>
            </div>
        % endfor
    % endif

    ${next.body()}
    <div id="footer">${self.footer()}</div>
</div>
</body>
</html>

<%def name="title()">troppo tardi - </%def>

<%def name="head()">
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<link rel="shortcut icon" href="/favicon.ico" />
<!--<script type="text/javscript" src="/js/mootools-core-1.3-full-compat.js"></script>-->

</%def>
<%def name="footer()"></%def>
