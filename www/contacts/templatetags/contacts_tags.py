# -*- coding: utf-8 -*-

from django import template
from django.template import Node
from django.template import TemplateSyntaxError

from contacts.models import Contacts

register = template.Library()

####################################################################################################
####################################################################################################


class ContactsGetItemNode(Node):
    def __init__(self, name):
        self.name = name
        super(ContactsGetItemNode, self).__init__()

    def render(self, context):
        """
        выводит список контактной информации в шаблон
        :type context: django.template.context.RequestContext
        """
        contacts = Contacts.objects.get_or_create(id=1)[0]
        context[self.name] = contacts
        return ''


def get_contact_info(parser, token):
    bits = token.split_contents()
    if len(bits) != 2:
        raise TemplateSyntaxError("%r != 2 argument" % bits[0])
    return ContactsGetItemNode(bits[1][1:-1])


get_contact_info = register.tag(get_contact_info)

####################################################################################################
####################################################################################################