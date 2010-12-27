import logging
from datetime import date

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators.rest import restrict, dispatch_on

from andreaciofi.lib.base import BaseController, render
from andreaciofi.lib import authorize
from andreaciofi.lib.helpers import flash
from andreaciofi.lib.images import store_image, remove_image, remove_image
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
        c.galleries = Gallery.by_created(self.db, descending=True)

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

            
        gallery.name = request.POST['name']
        gallery.text = request.POST['text']
        gallery.tags = [tag.strip() for tag in request.POST['tags'].split(',')]
        gallery.tags = filter(lambda t: t != '', gallery.tags)

        # cover image
        if hasattr(request.POST['cover_image'], 'file'):
            if gallery.cover:
                remove_image(gallery.cover)
            
            gallery.cover = store_image(request.POST['cover_image'].file)

        # other images
        for image in request.POST.getall('images'):
            if hasattr(image, 'file'):
                gallery.images.append(store_image(image.file))

        for image in request.POST.getall('delete_image'):
            gallery.images.remove(image)
            remove_image(image)

        # Video stuff
        for video in request.POST.getall('delete_video'):
            gallery.videos.remove(video)

        videos = [video.strip() for video in
                  request.POST['videos'].split(',')]
        videos = filter(lambda v: v != '', videos)

        if gallery.videos:
            gallery.videos.extend(videos)
        else:
            gallery.videos = videos
        

        gallery.date = date(int(request.POST['year']),
                            int(request.POST['month']),
                            1)

        gallery.store(self.db)

        flash("Gallery successfully edited.")
        redirect(url(controller='admin', action='galleries'))

    def delete_gallery(self, id):
        gallery = Gallery.load(self.db, id)

        remove_image(gallery.cover)

        self.db.delete(gallery)
        
        flash("Gallery successfully deleted.")
        redirect(url(controller='admin', action='galleries'))
