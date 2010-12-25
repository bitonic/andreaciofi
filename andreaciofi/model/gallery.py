import couchdb.mapping as mapping
from datetime import datetime


class Gallery(mapping.Document):
    type = mapping.TextField(default='Gallery')
    
    text = mapping.TextField()
    tags = mapping.ListField(mapping.TextField())
    images = mapping.ListField(mapping.TextField())
    videos = mapping.ListField(mapping.TextField())
    date = mapping.DateField()

    created = mapping.DateTimeField()
    modified = mapping.DateTimeField()

    def store(self, db):
        if not self.created:
            self.created = datetime.utcnow()
        else:
            self.modified = datetime.utcnow()
        
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
