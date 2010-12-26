import logging
from datetime import date

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators.rest import restrict, dispatch_on

from andreaciofi.lib.base import BaseController, render
from andreaciofi.lib import authorize
from andreaciofi.model import Gallery

log = logging.getLogger(__name__)

class AdminController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/admin.mako')
        # or, return a string
        return 'Hello World'

    @dispatch_on(POST='_do_galleries')
    def galleries(self):
        c.galleries = Gallery.by_created(self.db)

        return render('/admin/galleries.mako')

    def new_gallery(self):
        return render('/admin/new_gallery.mako')

    def edit_gallery(self, id):
        c.gallery = Gallery.load(self.db, id)
        return render('/admin/edit_gallery.mako')

    @restrict('POST')
    def do_edit_gallery(self, id=None):
        if not id:
            gallery = Gallery()
        else:
            gallery = Gallery.load(self.db, id)
        
        gallery.name = request.POST.get('name')
        gallery.text = request.POST.get('text')

        tags = request.POST.get('tags').split(',')
        tags = [tag.strip() for tag in tags]
        gallery.tags = tags

        gallery.date = date(int(request.POST.get('year')),
                            int(request.POST.get('month')),
                            1)

        gallery.store(self.db)

        redirect(url(controller='admin', action='galleries'))
