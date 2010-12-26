"""Setup the andreaciofi application"""
import logging

from couchdb import Database
from couchdb.mapping import ViewDefinition

import pylons.test

from andreaciofi.config.environment import load_environment
from andreaciofi.model import Gallery

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    config = load_environment(conf.global_conf, conf.local_conf)

    print "Syncing the couchdb database..."
    db = Database(config['couchdb_uri'])
    ViewDefinition.sync_many(db, [
            Gallery.by_date, Gallery.by_created, Gallery.by_slug,
            ])
