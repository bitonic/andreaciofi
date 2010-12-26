import couchdb.mapping as mapping
from datetime import datetime

class Gallery(mapping.Document):
    type = mapping.TextField(default='Gallery')
    
    name = mapping.TextField()
    text = mapping.TextField()
    tags = mapping.ListField(mapping.TextField())
    images = mapping.ListField(mapping.TextField())
    videos = mapping.ListField(mapping.TextField())
    date = mapping.DateField()

    created = mapping.DateTimeField()
    modified = mapping.DateTimeField()
    slug = mapping.TextField()

    def store(self, db):
        if not self.created:
            self.created = datetime.utcnow()
        else:
            self.modified = datetime.utcnow()

        if not self.slug:
            self.slug = self.date.strftime("%Y-%m")

            oldslug = list(Gallery.by_slug(db, startkey=self.slug, limit=1))
            if oldslug:
                oldslug = oldslug[0].slug
            counter = 1
            while oldslug == self.slug:
                self.slug = self.date.strftime("%Y-%m") + '_' + str(counter)
                oldslug = list(Gallery.by_slug(db, startkey=self.slug, limit=1))
                if oldslug:
                    oldslug = oldslug[0].slug
                else:
                    break
                counter += 1
        
        super(Gallery, self).store(db)
        
        return self

    by_date = mapping.ViewField('galleries', '''
        function(doc) {
            if (doc.type == 'Gallery') {
                emit(doc.date, doc);
            }
        }''')

    by_created = mapping.ViewField('galleries', '''
        function(doc) {
            if (doc.type == 'Gallery') {
                emit(doc.created, doc);
            }
        }''')

    by_slug = mapping.ViewField('galleries', '''
        function(doc) {
            if (doc.type == 'Gallery') {
                emit(doc.slug, doc);
            }
        }''')
