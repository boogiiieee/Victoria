# -*- coding: utf-8 -*-

from django.template.base import Node, NodeList, Template, Context, Variable
from django.template.defaulttags import token_kwargs
from django import template
import re

register = template.Library()

#######################################################################################################################
#######################################################################################################################

class paginate_split_list_node(Node):
	def __init__(self, page_range, page):
		self.page_range = template.Variable(page_range)
		self.page = template.Variable(page)

	def render(self, context):
		page_range = self.page_range.resolve(context)
		page = self.page.resolve(context)
		page_count = len(page_range)
		
		prev1, next1 = False, False
		if page > 1: prev1 = page - 1
		if page < page_count: next1 = page + 1
		
		if page_count > 10:
			if page < 5 or page > page_count-4:
				new_page_range = [[page_range[:5],True], [page_range[-5:],False]]
			else:
				new_page_range = [[page_range[:3],True], [page_range[page-2:page+1],True], [page_range[-3:],False]]
		else:
			new_page_range = [[page_range],False]
		
		context['paginate_page_range'] = [new_page_range, prev1, next1]
		return ''
		
def paginate_split_list(parser, token):
	bits = list(token.split_contents())
	if len(bits) != 3:
		raise TemplateSyntaxError("%r takes < 3 arguments" % bits[0])
	return paginate_split_list_node(bits[1], bits[2])
	
paginate_split_list = register.tag(paginate_split_list)

#######################################################################################################################
#######################################################################################################################

class get_url_node(Node):
	def __init__(self, extra_context=None):
		self.extra_context = extra_context or {}

	def render(self, context):
		g = context.get('request').GET
		e = g.copy()
			
		for key, val in self.extra_context.iteritems():
			try:
				val = val.resolve(context)
			except:
				pass

			if key:
				if val == 'None':
					if key in e: del e[key]
				else:
					e[key] = val
		
		u = e.urlencode()
		return u'?%s' % u if u else u''
		
def get_url(parser, token):
	bits = token.split_contents()
	remaining_bits = bits[1:]
	extra_context = token_kwargs(remaining_bits, parser, support_legacy=True)
	if not extra_context:
		raise TemplateSyntaxError("%r expected at least one variable assignment" % bits[0])
	if remaining_bits:
		raise TemplateSyntaxError("%r received an invalid token: %r" % (bits[0], remaining_bits[0]))
	return get_url_node(extra_context)
	
get_url = register.tag(get_url)

#######################################################################################################################
#######################################################################################################################