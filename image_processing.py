import numpy as np
from PIL import Image, ImageOps, ImageChops


def trim_borders(image):
    bg = Image.new(image.mode, image.size, image.getpixel((0,0)))
    diff = ImageChops.difference(image, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return image.crop(bbox)
    
    return image

def pad_image(image):
    return ImageOps.expand(image, border=30, fill='#fff')

def to_grayscale(image):
    return image.convert('L')

def invert_colors(image):
    return ImageOps.invert(image)

def resize_image(image):
    return image.resize((28, 28), Image.LINEAR)


def process_image(path):
    image = Image.open(path)
    image = trim_borders(image)
    image = pad_image(image)
    image = to_grayscale(image)
    #image = invert_colors(image)
    image = resize_image(image)
    image.save('testImg.png')
    return np.array([
        np.array(image).flatten()
    ])
