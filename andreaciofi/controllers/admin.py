import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from andreaciofi.lib.base import BaseController, render

log = logging.getLogger(__name__)

class AdminController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/admin.mako')
        # or, return a string
        return 'Hello World'

    @authorize()
    @dispatch_on(POST='_do_pending')
    def galleries(self):
        c.galleries = Gallery.by_created(self.db, descending=True)

        return render('/admin/galleries.mako')
