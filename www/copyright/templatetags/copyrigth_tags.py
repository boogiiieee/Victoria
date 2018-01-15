# -*- coding: utf-8 -*-

from django import template
from django.template import Node
from django.template import TemplateSyntaxError


import datetime

register = template.Library()

####################################################################################################
####################################################################################################


class GetCopyrightNode(Node):
    def __init__(self, year):
        self.year = year

    def render(self, context):
        if str(self.year) == str(datetime.datetime.now().year):
            return '%s' % self.year
        else:
            return '%s - %s' % (self.year, datetime.datetime.now().year)


def get_copyright(parser, token):
    bits = token.split_contents()
    if len(bits) != 2:
        raise TemplateSyntaxError('Error token tag "get_copyright"')

    return GetCopyrightNode(bits[1])


get_copyright = register.tag(get_copyright)

####################################################################################################
####################################################################################################