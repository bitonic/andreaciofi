import couchdb.mapping as mapping
from datetime import datetime

from andreaciofi.lib.images import remove_image

class Gallery(mapping.Document):
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

    def remove_image(self, image):
        self.images.remove(image)
        remove_image(image)

    def delete(self, db):
        try:
            remove_image(self.cover)
        except Exception:
            pass

        for image in self.images:
            try:
                remove_image(image)
            except Exception:
                pass

        db.delete(self)

    @property
    def all_tags(self):
        all_tags = self.tags
        all_tags.append(self.date.strftime('%Y'))
        if len(self.videos) > 0:
            all_tags.append('video')
        return all_tags
                        
    
    by_date = mapping.ViewField('galleries', '''
        function(doc) {
            emit(doc.date, {
               cover: doc.cover,
               date: doc.date,
               tags: doc.tags,
               name: doc.name,
               slug: doc.slug,
               videos: doc.videos,
            });
        }''')

    by_created = mapping.ViewField('galleries', '''
        function(doc) {
            emit(doc.created, doc);
        }''')

    by_slug = mapping.ViewField('galleries', '''
        function(doc) {
            emit(doc.slug, {
                name: doc.name,
                text: doc.text,
                tags: doc.tags,
                images: doc.images,
                videos: doc.videos,
                date: doc.date,
                slug: doc.slug,
            });
        }''')

    count = mapping.ViewField('galleries', '''
        function(doc) {
            emit("count", 1);
        }''', '''
        function(keys, values, rereduce) {
            return sum(values);
        }''')

    tag_count = mapping.ViewField('galleries', '''
        function(doc) {
            for (var i in doc.tags) {
                emit(doc.tags[i], 1);
            }
            emit(doc.date.substr(0, 4), 1);
            if (doc.videos.length > 0) {
                emit("video", 1);                
            }
        }''', '''
        function(keys, values, rereduce) {
            return sum(values);
        }''')

    by_tag = mapping.ViewField('galleries', '''
        function(doc) {
            for (var i in doc.tags) {
                emit([doc.tags[i], doc.date], {
                    cover: doc.cover,
                    date: doc.date,
                    tags: doc.tags,
                    name: doc.name,
                    slug: doc.slug,
                    videos: doc.videos,
                });
            }
            emit([doc.date.substr(0, 4), doc.date], {
                cover: doc.cover,
                date: doc.date,
                tags: doc.tags,
                name: doc.name,
                slug: doc.slug,
                videos: doc.videos,
            });
            if (doc.videos.length > 0) {
                emit(["video", doc.date], {
                    cover: doc.cover,
                    date: doc.date,
                    tags: doc.tags,
                    name: doc.name,
                    slug: doc.slug,
                    videos: doc.videos,
                });                
            }
        }''')

    years = mapping.ViewField('galleries', '''
        function(doc) {
            var year = parseInt(doc.date.substr(0, 4), 10);
            emit(year, 0);
        }''', '''
        function(keys, values, rereduce) {
            return 0;
        }''')
