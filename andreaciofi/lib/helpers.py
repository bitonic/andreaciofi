"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
from webhelpers.html.tags import *
from webhelpers.pylonslib import Flash as _Flash
from webhelpers.html import literal
from datetime import datetime
from docutils.core import publish_parts

from pylons import url, session

from andreaciofi.lib.images import thumbnailer, image_url, image_size

flash = _Flash()

def truncate_string(content, length=100, suffix='...'):
    if len(content) <= length:
        return content
    else:
        return ' '.join(content[:length + 1].split(' ')[0:-1]) + suffix

def thumbnailer_url(name, **kwargs):
    return image_url(thumbnailer(name, **kwargs))

def process_text(text):
    return literal(publish_parts(text, writer_name="html")["html_body"])
