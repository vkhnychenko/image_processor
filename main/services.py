from io import BytesIO
import requests
from PIL import Image
from django.core.files.base import ContentFile


def get_image_from_url(url):
    r = requests.get(url, stream=True)
    r.raw.decode_content = True
    buf = BytesIO()
    buf.write(r.content)
    return buf


def resize_image(image_field, width=None, height=None):
    img = Image.open(image_field)
    if width and height:
        new_img = img.resize((int(width), int(height)), Image.ANTIALIAS)
    elif width:
        ratio = (int(width) / float(img.size[0]))
        img_height = int((float(img.size[1]) * float(ratio)))
        new_img = img.resize((int(width), img_height), Image.ANTIALIAS)
    elif height:
        ratio = (int(height) / float(img.size[1]))
        img_width = int((float(img.size[0]) * float(ratio)))
        new_img = img.resize((img_width, int(height)), Image.ANTIALIAS)
    buffer = BytesIO()
    new_img.save(fp=buffer, format='JPEG')
    return ContentFile(buffer.getvalue())