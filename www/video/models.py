# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.db import models
import os

from embed_video.fields import EmbedVideoField
from pytils.translit import slugify
from sorl.thumbnail import ImageField as SorlImageField

from videoplayer.fields import VideoField

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
        return u'upload/video/item/%s' % filename.lower()

    VIDEO_CHOICES = (
        ('URL', u'Ссылка на YouTube'),
        ('FILE', u'Видеофайл'),
    )

    category = models.CharField(max_length=4, choices=VIDEO_CHOICES, default='URL',
                                verbose_name=u'выводим на сайте')
    title = models.CharField(max_length=100, verbose_name=u'заголовок')

    video_url = EmbedVideoField(blank=True, verbose_name=u'Видео-ссылка')
    video_file = VideoField(upload_to=make_upload_path,
                            help_text=u'Разрешенные к загрузке файлы: <b>avi, mp4</b>',
                            blank=True, verbose_name=u'Видео-файл')
    image = SorlImageField(upload_to=make_upload_path, verbose_name=u'изображение',
                           help_text=u'Изображение для превью видеофайла, будет показано на '
                                     u'месте вывода видео до начала просмотра',
                           blank=True)

    is_active = models.BooleanField(verbose_name=u'активно', default=True)
    sort = models.IntegerField(verbose_name=u'порядок', default=0)

    objects = models.Manager()
    activs = ActiveManager()

    def get_category(self):
        return self.category

    def get_title(self):
        return self.title

    def get_slug(self):
        return self.slug

    def get_video_url(self):
        return self.video_url

    def get_video_file(self):
        return self.video_file


    def __unicode__(self):
        return u'%s' % self.title

    @models.permalink
    def get_absolute_url(self):
        return 'video_list_url', (), {}

    def get_admin_url(self):
        return reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.module_name),
                       args=[self.id])

    class Meta:
        verbose_name = u'видео'
        verbose_name_plural = u'видео'
        ordering = ['sort', '-id']

####################################################################################################
####################################################################################################