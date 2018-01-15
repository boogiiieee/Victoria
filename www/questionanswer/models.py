# -*- coding: utf-8 -*-

from django.db import models
from ckeditor.fields import RichTextField

####################################################################################################
####################################################################################################


class ActiveManager(models.Manager):
    def get_query_set(self):
        return super(ActiveManager, self).get_query_set().filter(is_active=True)

####################################################################################################
####################################################################################################


class Subject(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'тема')

    is_active = models.BooleanField(verbose_name=u'активно', default=True)
    sort = models.IntegerField(verbose_name=u'порядок', default=0)

    objects = models.Manager()
    activs = ActiveManager()

    def get_title(self):
        return self.title

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        verbose_name = u'тема'
        verbose_name_plural = u'темы'
        ordering = ['sort', 'id']

####################################################################################################
####################################################################################################


class Item(models.Model):
    subject = models.ForeignKey(Subject, verbose_name=u'тема')
    name = models.CharField(max_length=100, verbose_name=u'ФИО')
    email = models.CharField(max_length=100, verbose_name=u'e-mail', blank=True)
    phone = models.CharField(max_length=100, verbose_name=u'телефон', blank=True)

    question = RichTextField(max_length=1000, verbose_name=u'вопрос')
    date_question = models.DateTimeField(verbose_name=u'дата вопроса', auto_now_add=True)

    name_answer = models.CharField(max_length=100, verbose_name=u'ФИО ответившего', blank=True)
    answer = RichTextField(max_length=1000, verbose_name=u'ответ', blank=True)
    date_answer = models.DateTimeField(verbose_name=u'дата ответа', blank=True, null=True)

    is_active = models.BooleanField(verbose_name=u'активно', default=False)
    sort = models.IntegerField(verbose_name=u'порядок', default=0)

    objects = models.Manager()
    activs = ActiveManager()

    def __unicode__(self):
        return u'%s' % self.subject

    def get_subjects(self):
        return self.subject

    def get_question(self):
        return self.question

    def get_answer(self):
        return self.answer

    @models.permalink
    def get_absolute_url(self):
        return ('question_url', (), {})

    class Meta:
        verbose_name = u'вопрос-ответ'
        verbose_name_plural = u'вопрос-ответ'
        ordering = ['sort', '-date_question', '-date_answer', '-id']


####################################################################################################
####################################################################################################