<%inherit file="/admin/base.mako" />

<%def name="title()">${parent.title()} - Login</%def>

<%def name="heading()">Login</%def>

% if c.logged_in:
    <b>You are already logged in.</b>
% else:
    ${h.form(h.url(controller='admin', action='login'), method='POST')}
    Username: ${h.text('username')}<br/>
    Password: ${h.password('password')}<br/>
    ${h.submit('submit', 'Submit')}
    ${h.end_form()}
% endif
