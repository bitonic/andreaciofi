"""The base Controller API

Provides the BaseController class for subclassing.
"""
from pylons.controllers import WSGIController
from pylons.templating import render_mako as render
from pylons import tmpl_context as c, config

from couchdb import Database

class BaseController(WSGIController):

    def __call__(self, environ, start_response):
        """Invoke the Controller"""

        # Set up the database object
        c.db = self.db = Database(config['couchdb_uri'])
        
        # WSGIController.__call__ dispatches to the Controller method
        # the request is routed to. This routing information is
        # available in environ['pylons.routes_dict']
        return WSGIController.__call__(self, environ, start_response)
