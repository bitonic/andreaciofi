import logging

from pylons import request, response, session, tmpl_context as c, url, config
from pylons.controllers.util import abort, redirect

from andreaciofi.lib.base import BaseController, render
from andreaciofi.model import Gallery

log = logging.getLogger(__name__)

# This code is really, really ugly. I should restructure it with a
# common function to list galleries with an optional tag parameter and
# the possibility to switch between the two listing modes.

class GalleryController(BaseController):
    entries_per_page = 10
    
    def __before__(self):
        c.years = list(self.db.view('galleries/years', group=True, descending=True))
        for i in range(len(c.years)):
            c.years[i] = c.years[i].key

        c.analytics_id = config['analytics_id']

    def index(self):
        redirect(url(controller='gallery', action='list', page=1))

    def list(self, page, tag=None):
        try:
            int(page)
        except ValueError:
            abort(404)

        c.pages = list(self.db.view('galleries/count'))

        c.pages = list(self.db.view('galleries/count'))[0].value
        c.pages = (c.pages % self.entries_per_page == 0) and \
            list(self.db.view('galleries/count'))[0].value / self.entries_per_page or \
            list(self.db.view('galleries/count'))[0].value / self.entries_per_page + 1

        if int(page) <= c.pages:
            c.galleries = list(Gallery.by_date(
                    self.db,
                    descending=True,
                    limit=self.entries_per_page,
                    skip=self.entries_per_page * (int(page) - 1)
                    ))
            c.pages = (c.pages % self.entries_per_page == 0) and \
                list(self.db.view('galleries/count'))[0].value / self.entries_per_page or \
                list(self.db.view('galleries/count'))[0].value / self.entries_per_page + 1
            c.page = int(page)
            
            c.base_url = url(controller='gallery', action='list', page=0)[:-1]
            
            return render('/gallery/gallery_list.mako')
        else:
            abort(404)
                                           

    def tag(self, tag, page=0):
        try:
            int(page)
        except ValueError:
            abort(404)

        c.pages = list(self.db.view('galleries/tag_count',
                                    group=True, key=tag))
        if c.pages:
            c.pages = c.pages[0].value
            c.pages = (c.pages % self.entries_per_page == 0) and \
                list(self.db.view('galleries/tag_count', group=True, key=tag))[0].value / self.entries_per_page or \
                list(self.db.view('galleries/tag_count', group=True, key=tag))[0].value / self.entries_per_page + 1
            page = int(page)
            if page <= c.pages:
                if page == 0:
                    redirect(url(controller='gallery', action='tag', tag=tag, page=1))
                else:
                    c.galleries = list(Gallery.by_tag(
                            self.db,
                            descending=True,
                            startkey=[tag,{}],
                            endkey=[tag[:-1] + unichr(ord(tag[-1]) - 1)],
                            skip=self.entries_per_page * (int(page) - 1),
                            limit=self.entries_per_page,
                            ))

                    c.page = page
                    c.base_url = url(controller='gallery', action='tag', tag=tag, page=0)[:-1]
                    
                    c.tag = tag
                    return render('/gallery/gallery_list.mako')
            else:
                abort(404)
        else:
            abort(404)

    def all_images(self, tag=None):
        c.tag = tag
        if tag:
            c.galleries = list(Gallery.by_tag(
                    self.db,
                    descending=True,
                    startkey=[tag,{}],
                    endkey=[tag[:-1] + unichr(ord(tag[-1]) - 1)],
                    ))
        else:
            c.galleries = list(Gallery.by_date(self.db, descending=True))

        return render('/gallery/all_images.mako')

    def show(self, slug):
        c.gallery = list(Gallery.by_slug(self.db, key=slug, limit=1))

        if not c.gallery or c.gallery[0].slug != slug:
            abort(404)
        else:
            c.gallery = c.gallery[0]
            
            return render('/gallery/show.mako')
    
    def about(self):
        return render('/about.mako')
