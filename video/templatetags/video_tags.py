# -*- coding: utf-8 -*-

from django import template
from django.template import Node, NodeList, Template, Context, Variable
from django.template import TemplateSyntaxError, Library

from video.models import  Item

register = template.Library()

#######################################################################################################################
#######################################################################################################################

#Список контактов в правую колонку
class VideoGetItemNode(Node):
	def __init__(self, name, *args, **kwargs):
		self.name = name
		super(VideoGetItemNode, self).__init__(*args, **kwargs)
		
	def render(self, context):
		video_list = Item.activs.all()
		context.update({'video_list':video_list})
		return ''

def get_video_list(parser, token):
	bits = token.split_contents()
	if len(bits) < 1: raise TemplateSyntaxError("%r != 1 argument" % bits[0])
	return VideoGetItemNode(bits[0])

get_video_list = register.tag(get_video_list)

#######################################################################################################################
#######################################################################################################################