# -*- coding: utf-8 -*-
import os

import re

from django.db import models
from django.core.urlresolvers import reverse

from pytils.translit import slugify

from map2gis.django_2gis_widget import LocationField

from sorl.thumbnail import ImageField as SorlImageField

####################################################################################################
####################################################################################################


class ActiveManager(models.Manager):
    def get_query_set(self):
        return super(ActiveManager, self).get_query_set().filter(is_active=True)

####################################################################################################
####################################################################################################


class Contacts(models.Model):
    """
    В Django 1.5 убрана проверка URLField на существование, проверяется только валидидность
      соответствия корректному URL
    """
    title = models.CharField(max_length=100, verbose_name=u'заголовок', blank=True,
                             default=u'Контактная информация')
    work_time = models.CharField(max_length=100, verbose_name=u'режим работы', blank=True)
    site = models.URLField(max_length=100, verbose_name=u'сайт', blank=True)
    desc_site = models.CharField(max_length=500, verbose_name=u'информация к сайту', blank=True)
    adress = LocationField(verbose_name=u'адрес', blank=True, null=True)
    alt_adress = models.CharField(max_length=500, verbose_name=u'альтернативный адрес',
                                  help_text=u'введите свое написание адреса, если хотите чтобы он \
                                            отличался от адреса, полученного из карты.',
                                  blank=True)
    desc_adress = models.CharField(max_length=500, verbose_name=u'информация к адресу', blank=True)

    objects = models.Manager()
    activs = ActiveManager()

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_work_time(self):
        return self.work_time

    def get_site(self):
        """
        вырезаем http и / на конце URL для отображения во фронтенде сайта
        """
        return re.sub(u'(^http://|/$)', u'', self.site)

    def get_full_site(self):
        return self.site

    def get_desc_site(self):
        return self.desc_site

    def get_adress(self):
        return self.adress

    def get_map_adress(self):
        """
        возвращает адрес, полученный из карты

        @return: adress['address']
        """
        return self.adress['address']

    def get_alt_adress(self):
        return self.alt_adress

    def get_desc_adress(self):
        return self.desc_adress

    def __unicode__(self):
        return u'%s' % self.get_title()

    def get_phones(self):
        return Phone.activs.filter(contacts=self)

    def get_skypes(self):
        return Skype.activs.filter(contacts=self)

    def get_emails(self):
        return Email.activs.filter(contacts=self)

    def get_socials(self):
        return Social.activs.filter(contacts=self)

    def get_admin_url(self):
        return reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.module_name),
                       args=[self.id])

    class Meta:
        verbose_name = u'контакт'
        verbose_name_plural = u'контакты'

####################################################################################################
####################################################################################################


class Phone(models.Model):
    contacts = models.ForeignKey(Contacts, verbose_name=u'контакты')
    phone = models.CharField(max_length=100, verbose_name=u'телефон', blank=True)
    desc_phone = models.CharField(max_length=500, verbose_name=u'информация к телефону', blank=True)
    is_active = models.BooleanField(verbose_name=u'активно', default=True)
    sort = models.IntegerField(verbose_name=u'порядок', default=0)

    objects = models.Manager()
    activs = ActiveManager()

    def get_phone(self):
        return self.phone

    def get_desc_phone(self):
        return self.desc_phone

    def __unicode__(self):
        return u'%s' % self.get_phone()

    class Meta:
        verbose_name = u'телефон'
        verbose_name_plural = u'телефоны'
        ordering = ['sort', 'id']

####################################################################################################
####################################################################################################


class Email(models.Model):
    contacts = models.ForeignKey(Contacts, verbose_name=u'контакты')
    email = models.EmailField(max_length=100, verbose_name=u'E-mail', blank=True)
    desc_email = models.CharField(max_length=500, verbose_name=u'информация к E-mail', blank=True)
    is_active = models.BooleanField(verbose_name=u'активно', default=True)
    sort = models.IntegerField(verbose_name=u'порядок', default=0)

    objects = models.Manager()
    activs = ActiveManager()

    def get_email(self):
        return self.email

    def get_desc_email(self):
        return self.desc_email

    def __unicode__(self):
        return u'%s' % self.get_email()

    class Meta:
        verbose_name = u'E-mail'
        verbose_name_plural = u'E-mail\'s'
        ordering = ['sort', 'id']

####################################################################################################
####################################################################################################


class Skype(models.Model):
    contacts = models.ForeignKey(Contacts, verbose_name=u'контакты')
    skype = models.CharField(max_length=100, verbose_name=u'skype', blank=True)
    desc_skype = models.CharField(max_length=500, verbose_name=u'информация к Skype', blank=True)
    is_active = models.BooleanField(verbose_name=u'активно', default=True)
    sort = models.IntegerField(verbose_name=u'порядок', default=0)

    objects = models.Manager()
    activs = ActiveManager()

    def get_skype(self):
        return self.skype

    def get_desc_skype(self):
        return self.desc_skype

    def __unicode__(self):
        return u'%s' % self.get_skype()

    class Meta:
        verbose_name = u'Skype'
        verbose_name_plural = u'Skype\'s'
        ordering = ['sort', 'id']

####################################################################################################
####################################################################################################


class Social(models.Model):
    def make_upload_path(instance, filename):
        name, extension = os.path.splitext(filename)
        filename = u'%s%s' % (slugify(name), extension)
        return u'upload/contacts/social/%s' % filename.lower()

    contacts = models.ForeignKey(Contacts, verbose_name=u'контакты')
    title = models.CharField(max_length=100, verbose_name=u'название', blank=True)
    social_url = models.URLField(max_length=100, verbose_name=u'ссылка', blank=True)
    icon = SorlImageField(upload_to=make_upload_path, verbose_name=u'иконка', blank=True)
    is_active = models.BooleanField(verbose_name=u'активно', default=True)
    sort = models.IntegerField(verbose_name=u'порядок', default=0)

    objects = models.Manager()
    activs = ActiveManager()

    def get_title(self):
        return self.title

    def get_social_url(self):
        return re.sub(u'(^http://|/$)', u'', self.social_url)

    def get_full_url(self):
        return self.social_url

    def get_icon(self):
        return self.icon

    def __unicode__(self):
        return u'%s' % self.get_title()

    class Meta:
        verbose_name = u'социальная сеть'
        verbose_name_plural = u'социальные сети'
        ordering = ['sort', 'id']

####################################################################################################
####################################################################################################