# -*- coding: utf-8 -*-

from django import template
from django.template import Node, NodeList, Template, Context, Variable
from django.template import TemplateSyntaxError
from django.utils.encoding import force_unicode
from django.conf import settings
import os, re

register = template.Library()

#######################################################################################################################
#######################################################################################################################

#Для администратора ставит ссылку на url	
class FrontAdminNode(Node):
	def __init__(self, url):
		self.url = url
		
	def render(self, context):
		request = context.get('request', None)
	
		if request and request.user and request.user.is_staff:
			try:
				url = template.Variable(self.url).resolve(context)
			except:
				try:
					url = self.url[1:-1]
				except:
					return u''
			return u'''
				<a class="frontadmin" href="%s" target="_blank" title="Редактировать" class="edit"><i class="icon-edit"></i></a>
			''' % url 
		else:
			return u''

def FrontAdmin(parser, token):
	bits = token.split_contents()
	if len(bits) != 2: raise TemplateSyntaxError('Error token tag "FrontAdmin"')
	return FrontAdminNode(bits[1])

register.tag('FrontAdmin', FrontAdmin)

#######################################################################################################################
#######################################################################################################################