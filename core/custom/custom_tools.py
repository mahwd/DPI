from time import time


def get_social_icon_path(instance, filename):

    return "social_icons/%s_%s" % (str(time()).replace('.', '_'), filename.replace(' ', '_'))
