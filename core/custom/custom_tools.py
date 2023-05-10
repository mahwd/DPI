from time import time
from django.utils.html import mark_safe


def get_social_icon_path(instance, filename):
    return "social_icons/%s_%s" % (str(time()).replace('.', '_'), filename.replace(' ', '_'))


def get_carousel_image(instance, filename):
    return "carousel_image/%s_%s" % (str(time()).replace('.', '_'), filename.replace(' ', '_'))


def get_brand_image(instance, filename):
    return "brand_image/%s_%s" % (str(time()).replace('.', '_'), filename.replace(' ', '_'))


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
