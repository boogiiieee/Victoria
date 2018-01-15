# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
import os

from embed_video.fields import EmbedVideoField
from pytils.translit import slugify

from videoplayer.fields import VideoField

################################################################################################
################################################################################################

class ActiveManager(models.Manager): 
	def get_query_set(self): 
		return super(ActiveManager, self).get_query_set().filter(is_active=True)

################################################################################################################
################################################################################################################
		
class Item(models.Model):
	
	def make_upload_path(instance, filename):
		name, extension = os.path.splitext(filename)
		filename = u'%s%s' % (slugify(name), extension)
		return u'upload/video/item/%s' % filename.lower()
		
	VIDEO_CHOICES = (
		('URL', u'Ссылка на YouTube'),
		('FILE', u'Видеофайл'),
	)
	
	category = models.CharField(max_length=100, choices=VIDEO_CHOICES, default='URL', verbose_name=u'категория')
	title = models.CharField(max_length=100, verbose_name=u'заголовок')
	
	video_url = EmbedVideoField()
	file = VideoField(upload_to=make_upload_path,  help_text=u'разрешенные к загрузке файлы: avi, mp4', blank=True)

	is_active = models.BooleanField(verbose_name=u'активно', default=True)
	sort = models.IntegerField(verbose_name=u'порядок', default=0)
	
	objects = models.Manager()
	activs = ActiveManager()
	
	def get_category(self): return self.category
	
	def __unicode__(self):
		return u'%s' % self.title
	
	def get_admin_url(self):
		return reverse('admin:%s_%s_change' % (self._meta.app_label,  self._meta.module_name),  args=[self.id] )
		
	class Meta: 
		verbose_name = u'видео' 
		verbose_name_plural = u'видео'
		ordering = ['sort', 'id']
		
################################################################################################################
################################################################################################################