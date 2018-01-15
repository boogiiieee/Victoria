# -*- coding: utf-8 -*-

from django import template
from django.template import Node, NodeList, Template, Context, Variable
from django.template import TemplateSyntaxError
from django.template.loader import get_template
from django.conf import settings
import string
import random

register = template.Library()

from videoplayer.conf import settings as videoplayer_conf

####################################################################################################

####################################################################################################


#Возвращает случайную строку
def randdigits(n):
    a = string.digits
    return ''.join([random.choice(a) for i in range(n)])

####################################################################################################
####################################################################################################


#Подключает необходимые файлы для работы приложения
class VideoPlayerMediaNode(Node):
    def __init__(self):
        pass

    def render(self, context):
        return u'<script type="text/javascript" src="%(static)sjs/videoplayer/jwplayer.js">' \
               u'</script>' % {'static': settings.STATIC_URL}


def VideoPlayerMedia(parser, token):
    bits = token.split_contents()
    if len(bits) > 1:
        raise TemplateSyntaxError(u"ошибка тега %s" % bits[0])
    return VideoPlayerMediaNode()


register.tag('VideoPlayerMedia', VideoPlayerMedia)

####################################################################################################
####################################################################################################


#Выводит видео
class VideoFileNode(Node):
    def __init__(self, file_url, width, image_url, config=None):
        self.file_url = template.Variable(file_url)
        self.image_url = template.Variable(image_url)
        self.width = template.Variable(width)
        self.config = config

    def render(self, context):
        try:
            config = template.Variable(self.config).resolve(context)
        except:
            config = videoplayer_conf.DEFAULT_CONFIG

        t = get_template('videoplayer.html')
        c = t.render(Context({
            'file': self.file_url.resolve(context),
            'image': self.image_url.resolve(context),
            'width': self.width,
            'config': config,
            'id': randdigits(10),
            'STATIC_URL': settings.STATIC_URL,
            'MEDIA_URL': settings.MEDIA_URL
        }))

        return c


def VideoFile(parser, token):
    bits = token.split_contents()
    if len(bits) < 3:
        raise TemplateSyntaxError(u"ошибка тега %s, меньше 3 аргумента" % bits[0])
    try:
        config = bits[3]
    except:
        config = None
    return VideoFileNode(bits[1], bits[2][1:-1], config)


VideoFile = register.tag(VideoFile)