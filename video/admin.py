# -*- coding: utf-8 -*-

from django.contrib import admin
from embed_video.admin import AdminVideoMixin

from video.models import Item

################################################################################################################
################################################################################################################
	
class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
	list_display = ('category', 'is_active', 'sort')
	fieldsets = (
		(None, {'fields': ('category', 'title_embed', 'video_url', 'title_file', 'file', 'sort')},),
	)
	
admin.site.register(Item, VideoAdmin)

################################################################################################################
################################################################################################################