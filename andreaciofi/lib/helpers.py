"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
from webhelpers.html.tags import *
from webhelpers.pylonslib import Flash as _Flash
from webhelpers.html import literal
from datetime import datetime
from cgi import escape

from pylons import url

from andreaciofi.lib.images import thumbnailer, image_url, image_size
from andreaciofi.lib.bbcode import BBCode

flash = _Flash()

def truncate_string(content, length=100, suffix='...'):
    if len(content) <= length:
        return content
    else:
        return ' '.join(content[:length + 1].split(' ')[0:-1]) + suffix

def thumbnailer_url(name, **kwargs):
    return image_url(thumbnailer(name, **kwargs))

def process_text(text):
    result = escape(text)
    result = BBCode(text).generate_html()
    result = literal("<p>" + result[0] + "<p/><p>".join(result[1:].splitlines()) + "</p>")
    return result

def tags(tags):
    html = ""
    if tags:
        for tag in tags[:-1]:
            html += '<a href="' + \
                url(controller='gallery', action='tag', tag=tag) + '">' + tag \
                + '</a>, '
        html += '<a href="' + url(controller='gallery', action='tag', tag=tags[-1]) \
            + '">' + tags[-1] + '</a>.'
    return literal(html)
