import logging
from datetime import date
from decorator import decorator
from hashlib import sha1

from pylons import request, response, session, tmpl_context as c, url, config
from pylons.controllers.util import abort, redirect
from pylons.decorators.rest import restrict, dispatch_on
from pylons.decorators import validate

from andreaciofi.lib.base import BaseController, render
from andreaciofi.lib import authorize
from andreaciofi.lib.helpers import flash
from andreaciofi.lib.images import store_image, remove_image, remove_image
from andreaciofi.model import Gallery
from andreaciofi.model.forms import NewGallery, EditGallery

log = logging.getLogger(__name__)

def authorize():
    def validator(func, *args, **kwargs):
        # If the visitor is not logged in, redirect him to the login page
        if 'logged_in' not in session:
            session['redirect_to'] = request.environ.get('PATH_INFO')

            if request.environ.get('QUERY_STRING'):
                session['redirect_to'] += '?' + request.environ['QUERY_STRING']
            session.save()

            redirect(url(controller='admin', action='login'))
        else:
            return func(*args, **kwargs)

    return decorator(validator)    

class AdminController(BaseController):

    def index(self):
        redirect(url(controller='admin', action='galleries'))

    @authorize()
    def galleries(self):
        c.galleries = Gallery.by_created(self.db, descending=True)

        return render('/admin/galleries.mako')

    @authorize()
    def new_gallery(self):
        return render('/admin/new_gallery.mako')

    @authorize()
    def edit_gallery(self, id):
        c.gallery = Gallery.load(self.db, id)
        return render('/admin/edit_gallery.mako')

    @authorize()
    @restrict('POST')
    @validate(schema=NewGallery(), form='new_gallery')
    def do_new_gallery(self):
        self.do_edit_gallery()

    @authorize()
    @restrict('POST')
    @validate(schema=EditGallery(), form='edit_gallery')
    def do_edit_gallery(self, id=None):
        if not id:
            gallery = Gallery()
        else:
            gallery = Gallery.load(self.db, id)

            
        gallery.name = request.POST['name']
        gallery.text = request.POST['text']
        gallery.tags = [tag.strip().lower() for tag in request.POST['tags'].split(',')]
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

    @authorize()
    def delete_gallery(self, id):
        gallery = Gallery.load(self.db, id)

        gallery.delete(self.db)

        flash("Gallery successfully deleted.")
        redirect(url(controller='admin', action='galleries'))

    @dispatch_on(POST='_do_login')
    def login(self):
        return render('/admin/login.mako')

    @restrict('POST')
    def _do_login(self):
        if request.POST['username'] == config['admin_user'] and \
                sha1(request.POST['password']).hexdigest() == config['admin_password']:
            session['logged_in'] = True
            session.save()

            if 'redirect_to' in session:
                redirect_to = session['redirect_to']
                del session['redirect_to']
                session.save()
                redirect(redirect_to)
            else:
                redirect(url(controller='admin', action='galleries'))
        else:
            flash("Wrong username/password.")
            redirect(url(controller='admin', action='login'))

    def logout(self):
        del session['logged_in']
        session.save()

        redirect('/')
