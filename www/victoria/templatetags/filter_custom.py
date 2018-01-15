# coding=utf-8
from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

####################################################################################################
####################################################################################################

@register.filter()
def first_word_orange(text, autoescape=None):
    """
    Первое слово - оранжевым.
    Если первое слово <= 3 символам, то берем первые два слова.

    @type text: unicode
    @type autoescape: __builtin__.NoneType
    @param text:
    @param autoescape:None
    @return: <span class="f_orange">first word</span>...
    """
    text = text.split()
    first = text[0]
    if len(first[0:]) <= 3:
        first = text[0] + ' ' + text[1]
    else:
        first = text[0]

    other = ' '.join(text).replace(first, '', 1)
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    result = '<span class="f_orange">%s</span> %s' % (esc(first), esc(other))
    return mark_safe(result)

####################################################################################################
####################################################################################################