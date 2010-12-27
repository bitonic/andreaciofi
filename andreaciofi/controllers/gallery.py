import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from andreaciofi.lib.base import BaseController, render
from andreaciofi.model import Gallery

log = logging.getLogger(__name__)

class GalleryController(BaseController):
    entries_per_page = 10

    def index(self):
        c.galleries = list(Gallery.by_date(self.db, descending=True))

        return render('/gallery/gallery_list.mako')

    def show(self, slug):
        c.gallery = list(Gallery.by_slug(self.db, startkey=slug, limit=1))

        if not c.gallery or c.gallery[0].slug != slug:
            abort(404)
        else:
            c.gallery = c.gallery[0]
            
            return render('/gallery/show.mako')
