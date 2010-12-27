import couchdb.mapping as mapping
from datetime import datetime

class Gallery(mapping.Document):
    type = mapping.TextField(default='Gallery')
    
    name = mapping.TextField()
    text = mapping.TextField()
    tags = mapping.ListField(mapping.TextField())
    cover = mapping.TextField()
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
                emit(doc.date, {
                   cover: doc.cover,
                   date: doc.date,
                   tags: doc.tags,
                   name: doc.name,
                   slug: doc.slug,
                });
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
                emit(doc.slug, {
                    name: doc.name,
                    text: doc.text,
                    tags: doc.tags,
                    images: doc.images,
                    videos: doc.videos,
                    date: doc.date,
                    slug: doc.slug,
                });
            }
        }''')

    count = mapping.ViewField('galleries', '''
        function(doc) {
            if (doc.type == 'Gallery') {
                emit("count", 1);
            }
        }''', '''
        function(keys, values, rereduce) {
            return sum(values);
        }''')

    tag_count = mapping.ViewField('galleries', '''
        function(doc) {
            if (doc.type == 'Gallery') {
                for (var i in doc.tags) {
                    emit(doc.tags[i], 1);
                }
                emit(doc.date.substr(0, 4), 1);
                if (doc.videos.length > 0) {
                    emit("video", 1);                
                }
            }
        }''', '''
        function(keys, values, rereduce) {
            return sum(values);
        }''')

    by_tag = mapping.ViewField('galleries', '''
        function(doc) {
            if (doc.type == 'Gallery') {
                for (var i in doc.tags) {
                    emit([doc.tags[i], doc.date], {
                        cover: doc.cover,
                        date: doc.date,
                        tags: doc.tags,
                        name: doc.name,
                        slug: doc.slug,
                    });
                }
                emit([doc.date.substr(0, 4), doc.date], {
                    cover: doc.cover,
                    date: doc.date,
                    tags: doc.tags,
                    name: doc.name,
                    slug: doc.slug,
                });
                if (doc.videos.length > 0) {
                    emit(["video", doc.date], {
                        cover: doc.cover,
                        date: doc.date,
                        tags: doc.tags,
                        name: doc.name,
                        slug: doc.slug,
                    });                
                }
            }
        }''')

    years = mapping.ViewField('galleries', '''
        function(doc) {
            if (doc.type == 'Gallery') {
                var year = parseInt(doc.date.substr(0, 4), 10);
                emit(year, 1);
            }
        }''', '''
        function(keys, values, rereduce) {
            return sum(values);
        }''')
