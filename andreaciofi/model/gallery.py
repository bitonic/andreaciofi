import couchdb.mapping as mapping


class Gallery(mapping.Document):
    type = mapping.TextField(default='Gallery')
    
    text = mapping.TextField()
    tags = mapping.ListField(mapping.TextField())
    images = mapping.ListField(mapping.TextField())
    videos = mapping.ListField(mapping.TextField())
    date = mapping.DateField()
    created = mapping.DateTimeField()

    def store(self, db):
        
        super(Gallery, self).store(db)
        
        return self

    date = mapping.ViewField('galleries', '''
        function(doc) {
            if (doc.type == 'Gallery') {
                emit(doc.date, doc);
            }
        }''')

    created = mapping.ViewField('galleries', '''
        function(doc) {
            if (doc.type == 'Gallery') {
                emit(doc.created, doc);
            }
        }''')
