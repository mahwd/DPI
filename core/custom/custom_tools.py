from time import time
from django.utils.html import mark_safe
from io import BytesIO
from PIL import Image, ImageEnhance
from django.core.files import File


def optimise_image(image):
    # Open the image using PIL
    pil_image = Image.open(image)

    # Convert the image to RGB mode if it's not already
    if pil_image.mode != 'RGB':
        pil_image = pil_image.convert('RGB')

    # Resize the image to a maximum size of 1920x1080
    pil_image.thumbnail((1920, 1080))

    # Optimize the image and save it to a BytesIO buffer
    buffer = BytesIO()
    pil_image.save(buffer, format='JPEG', optimize=True, quality=90)
    buffer.seek(0)

    # Create a new InMemoryUploadedFile from the buffer and return it
    image_name = os.path.basename(image.name)
    return InMemoryUploadedFile(buffer, None, image_name, 'image/jpeg', buffer.getbuffer().nbytes, None)


def get_image_html(src, alt):
    if src:
        return mark_safe(
            "<img src='%s' style='width:auto;height:50px;' alt='%s' />" % (src, alt)
        )
    else:
        return mark_safe(
            "<img src='/static/images/no-image.png'"
            "style='width:75px;height:auto'"
            "-box.png' alt='image' />"
        )


def slugify(title):
    symbol_mapping = (
        (' ', '-'),
        ('.', '-'),
        (',', '-'),
        ('!', '-'),
        ('?', '-'),
        ("'", '-'),
        ('"', '-'),
        ('ə', 'e'),
        ('ı', 'i'),
        ('ö', 'o'),
        ('ğ', 'g'),
        ('ü', 'u'),
        ('ş', 's'),
        ('ç', 'c'),
    )

    title_url = title.strip().lower()

    for before, after in symbol_mapping:
        title_url = title_url.replace(before, after)

    return title_url
