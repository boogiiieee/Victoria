# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse
import os

from sorl.thumbnail import ImageField as SorlImageField
from ckeditor.fields import RichTextField
from pytils.translit import slugify

####################################################################################################
####################################################################################################


class ActiveManager(models.Manager):
    def get_query_set(self):
        return super(ActiveManager, self).get_query_set().filter(is_active=True)

####################################################################################################
####################################################################################################


class Item(models.Model):
    def make_upload_path(instance, filename):
        name, extension = os.path.splitext(filename)
        filename = u'%s%s' % (slugify(name), extension)
        return u'upload/article/item/%s' % filename.lower()

    title = models.CharField(max_length=500, verbose_name=u'заголовок')
    slug = models.CharField(max_length=500, verbose_name=u'псевдоним', unique=True)
    text = RichTextField(max_length=100000, verbose_name=u'текст')
    image = SorlImageField(upload_to=make_upload_path, verbose_name=u'изображение', blank=True)
    created_at = models.DateTimeField(verbose_name=u'дата создания', auto_now_add=True)
    is_active = models.BooleanField(verbose_name=u'активно', default=True)
    sort = models.IntegerField(verbose_name=u'порядок', default=0)

    objects = models.Manager()
    activs = ActiveManager()

    description = models.TextField(u'описание', blank=True)
    keywords = models.TextField(u'ключевые слова', blank=True)

    def get_title(self):
        return self.title

    def get_slug(self):
        return self.slug

    def get_text(self):
        return self.text

    def get_image(self):
        return self.image

    def get_created_at(self):
        return self.created_at

    def get_description(self):
        return self.description

    def get_keywords(self):
        return self.keywords

    def __unicode__(self):
        return self.get_title()

    @models.permalink
    def get_absolute_url(self):
        return 'article_url', (), {'slug': self.slug}

    def get_admin_url(self):
        return reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.module_name),
                       args=[self.id])

    class Meta:
        verbose_name = u'статья'
        verbose_name_plural = u'статьи'
        ordering = ['sort', '-id']

####################################################################################################
####################################################################################################