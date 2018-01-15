# -*- coding: utf-8 -*-

from django import template
from django.template import Node, NodeList, Template, Context, Variable
from django.template import TemplateSyntaxError
from django.template import get_library, Library, InvalidTemplateLibrary
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render_to_response
import settings
import os
import re
import datetime
import string
import random

register = template.Library()

from videoplayer.conf import settings as videoplayer_conf

#######################################################################################################################
#######################################################################################################################

#Возвращает случайную строку
def randdigits(n):
    a = string.digits
    return ''.join([random.choice(a) for i in range(n)])
	
#######################################################################################################################
#######################################################################################################################

#Подключает необходимые файлы для работы приложения
class VideoPlayerMediaNode(Node):
	def __init__(self):
		pass

	def render(self, context):
		return u'<script type="text/javascript" src="%(static)sjs/videoplayer/jwplayer.js"></script>' % {'static':settings.STATIC_URL}

def VideoPlayerMedia(parser, token):
	bits = token.split_contents()
	if len(bits) > 1:
		raise TemplateSyntaxError(_("Error token tag \"VideoPlayerMedia\""))
	return VideoPlayerMediaNode()

register.tag('VideoPlayerMedia', VideoPlayerMedia)

#######################################################################################################################
#######################################################################################################################

#Выводит видео
class VideoFileNode(Node):
	def __init__(self, file_url, config=None):
		self.file_url = template.Variable(file_url)
		self.config = config

	def render(self, context):
		try: config = template.Variable(self.config).resolve(context)
		except: config = videoplayer_conf.DEFAULT_CONFIG

		return render_to_response('videoplayer.html', {
			'file':self.file_url.resolve(context),
			'config':config,
			'id':randdigits(10), 
			'STATIC_URL':settings.STATIC_URL
		})._get_content()
		
def VideoFile(parser, token):
	bits = token.split_contents()
	if len(bits) < 2:
		raise TemplateSyntaxError(_("Error token tag \"VideoFile\""))
	try: config = bits[2]
	except: config = None
	return VideoFileNode(bits[1], config)
	
VideoFile = register.tag(VideoFile)