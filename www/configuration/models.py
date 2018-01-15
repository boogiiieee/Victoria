# -*- coding: utf-8 -*-

from django.db import models

####################################################################################################
####################################################################################################


#Настройки
class ConfigModel(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'название сайта',
                             default=u'Название сайта')
    code_phone = models.CharField(max_length=10, verbose_name=u'телефонный код',
                                  help_text=u'Введите только код города, <b>без 8 или +7</b>',
                                  blank=True)
    phone = models.CharField(max_length=20, verbose_name=u'основной телефон',
                             help_text=u'Телефон, который будет отображаться в шапке и '
                                       u'подвале сайта', blank=True)
    email = models.EmailField(max_length=100, verbose_name=u'E-mail', blank=True)
    adress = models.CharField(max_length=300, verbose_name=u'адрес', help_text=u'Адрес, '
                                                                               u'который будет '
                                                                               u'отображаться в '
                                                                               u'шапке и подвале '
                                                                               u'сайта', blank=True)

    def __unicode__(self):
        return u'настройки'

    class Meta:
        verbose_name = u'настройки'
        verbose_name_plural = u'настройки'

####################################################################################################
####################################################################################################