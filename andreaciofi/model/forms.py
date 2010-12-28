import formencode
from formencode import validators
import imghdr

class ImageFormat(formencode.FancyValidator):
    """Verifies that the image submitted is an image"""
    def _to_python(self, value, state):
        image_type = imghdr.what(value.file)

        if not (image_type == 'png' or image_type == 'jpeg'):
            raise formencode.Invalid(
                'The file you submitted is not a image',
                value, state)
        return value

class NewGallery(formencode.Schema):
    # images/submit
    allow_extra_fields = True
    filter_extra_fields = False
    cover_image = ImageFormat(not_empty=True)
    name = validators.String(not_empty=True)

class EditGallery(formencode.Schema):
    # images/submit
    allow_extra_fields = True
    filter_extra_fields = False
    cover_image = ImageFormat()
    name = validators.String(not_empty=True)
