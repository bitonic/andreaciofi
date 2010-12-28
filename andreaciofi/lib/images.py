from PIL import Image
import os
from pylons import config
import shutil
import imghdr
from random import choice
from glob import glob
from string import ascii_letters

def image_size(filename):
    im = Image.open(os.path.join(config['images_dir'], filename))

    return im.size

def thumbnailer(filename, max_width=None, max_height=None, crop=False):
    """Given the filename of an image in the image dir, it thumbnails
    it and stores it in the thumbnails directory (both directories are
    defined in the ini file).  It then returns the url of the
    thumbnail."""
    
    name, ext = os.path.splitext(filename)

    name = name + '_' + str(max_width) + 'x' + str(max_height)

    if crop:
        name += '_crop_'

    name += ext

    # If the thumbnail already exists, don't create it.  This could be
    # dangerous if the image could be changed, but the image cannot be
    # changed right now, so it should be safe.
    if not os.path.isfile(os.path.join(config['images_dir'], name)):
        
        im = Image.open(os.path.join(config['images_dir'], filename))
        (width, height) = im.size
        
        # If the image is smaller then the max size, we don't touch it
        if not (width <= max_width and height <= max_height):
            if crop and max_width and max_height:
                if width / float(height) >= max_width / float(max_height):
                    thumb_height = max_height
                    thumb_width = width * max_height / height
                    sx = (thumb_width - max_width) / 2
                    up = 0
                    dx = sx + max_width
                    low = max_height
                else:
                    thumb_width = max_width
                    thumb_height = max_width * height / width
                    sx = 0
                    up = (thumb_height - max_height) /2
                    dx = max_width
                    low = max_height + up
                    
                im.thumbnail((thumb_width, thumb_height), Image.ANTIALIAS)
                im = im.crop((sx, up, dx, low))
            else:
                if max_width and max_height:
                    if width > height: max_height = None
                    else: max_width = None
                
                # Calculate the size...
                if max_width and not max_height:
                    max_height = height * max_width / width
                elif max_height and not max_width:
                    max_width = width * max_height / height
                
                im.thumbnail((max_width, max_height), Image.ANTIALIAS)

        # Save it 
        im.save(os.path.join(config['images_dir'], name))
            
    return name

def image_path(filename):
    return os.path.join(config['images_dir'], filename)

def image_url(filename):
    return os.path.join(config['images_base_url'], filename)

def store_image(image_file):
    # Get the image format...
    format = imghdr.what(image_file)
    # Only png and jpeg files. There is already a check with the validator
    # but you never know (:
    if format in ['png', 'jpeg']:
        
        chars = []
        for i in range(len(ascii_letters)):
            chars.append(ascii_letters[i])
        chars.extend(map(str, range(10)))

        filename = ''.join([choice(chars) for i in range(7)])
        filename = filename + '.' + format

        while os.path.isfile(image_path(filename)):
            filename = ''.join([choice(chars) for i in range(7)])
            filename = filename + '.' + format
        
        # Open the new file
        permanent_file = open(image_path(filename), 'w')
    
        # Copy the temp file to its destination
        shutil.copyfileobj(image_file, permanent_file)
        image_file.close() # close everything
        permanent_file.close()

        return filename
    else:
        raise ValueError('The image must be of png or jpeg formats.')

def remove_image(filename):
    # delete the image
    os.remove(image_path(filename))

    # delete thumbs
    thumbs = glob(os.path.join(config['images_dir'],
                               os.path.splitext(filename)[0]) + '_*')
    
    for thumb in thumbs:
        os.remove(thumb)
