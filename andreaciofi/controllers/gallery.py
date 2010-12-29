import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from andreaciofi.lib.base import BaseController, render
from andreaciofi.model import Gallery

log = logging.getLogger(__name__)

class GalleryController(BaseController):
    entries_per_page = 10
    
    def __before__(self):
        c.years = list(self.db.view('galleries/years', group=True, descending=True))
        for i in range(len(c.years)):
            c.years[i] = c.years[i].key

    def index(self):
        redirect(url(controller='gallery', action='list', page=1))

    def list(self, page):
        c.galleries = list(Gallery.by_date(
                self.db,
                descending=True,
                limit=self.entries_per_page * page,
                ))[self.entries_per_page * (int(page) - 1):self.entries_per_page * int(page)]
        c.pages = list(self.db.view('galleries/count'))[0].value
        c.pages = (c.pages % self.entries_per_page == 0) and \
            list(self.db.view('galleries/count'))[0].value / self.entries_per_page or \
            list(self.db.view('galleries/count'))[0].value / self.entries_per_page + 1
        c.page = int(page)

        c.base_url = url(controller='gallery', action='list', page=0)[:-1]

        return render('/gallery/gallery_list.mako')
                                           

    def tag(self, tag, page=0):
        if page == 0:
            redirect(url(controller='gallery', action='tag', tag=tag, page=1))
        else:
            c.galleries = list(Gallery.by_tag(
                    self.db,
                    descending=True,
                    startkey=[tag,{}],
                    endkey=[tag[:-1] + unichr(ord(tag[-1]) - 1)],
                    limit=self.entries_per_page * page,
                    ))[self.entries_per_page * (int(page) - 1):self.entries_per_page * int(page)]

            c.pages = len(self.db.view('galleries/tag_count', group=True, key=tag)) / self.entries_per_page + 1
            c.page = int(page)

            return render('/gallery/gallery_list.mako')
            
    def show(self, slug):
        c.gallery = list(Gallery.by_slug(self.db, startkey=slug, limit=1))

        if not c.gallery or c.gallery[0].slug != slug:
            abort(404)
        else:
            c.gallery = c.gallery[0]
            
            return render('/gallery/show.mako')
