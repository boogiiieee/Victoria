# -*- coding: utf-8 -*-

from django.db import models

from ckeditor.fields import RichTextField

####################################################################################################
####################################################################################################


class Block(models.Model):
    title = models.CharField(max_length=200, verbose_name=u'заголовок')
    text = RichTextField(verbose_name=u'текст')

    def get_title(self):
        return self.title

    def get_text(self):
        return self.text

    def __unicode__(self):
        return self.get_title()

    class Meta:
        verbose_name = u'модуль'
        verbose_name_plural = u'текстовые модули'
        ordering = ['title']

        ############################################################################################
        ############################################################################################