# -*- coding: utf-8 -*-

from django import template
from django.template.loader import get_template
from django.template import Node,  Context
from django.template import TemplateSyntaxError

from simpleblocks.models import Block

register = template.Library()

####################################################################################################
####################################################################################################


class GetSimpleBlockNode(Node):
    def __init__(self, id, template):
        self.id = id
        self.template = str(template) if template else 'simpleblocks/simpleblocks.html'

    def render(self, context):
        try:
            item = Block.objects.get(id=int(self.id))
        except:
            item = None
        t = get_template(self.template)
        c = t.render(Context({'item': item}))
        return c


def get_simpleblock(parser, token):
    bits = token.split_contents()
    if len(bits) < 2 or len(bits) > 3:
        raise TemplateSyntaxError('Error token tag "get_simpleblock"')

    template = bits[2][1:-1] if len(bits) >= 3 and bits[2] and len(bits[2]) >= 3 else ''

    return GetSimpleBlockNode(bits[1], template)


get_simpleblock = register.tag(get_simpleblock)

####################################################################################################
####################################################################################################
