# -*- coding: utf-8 -*-

from django.contrib import admin

from embed_video.admin import AdminVideoMixin
from sorl.thumbnail.admin import AdminImageMixin

from video.models import Item

####################################################################################################
####################################################################################################


class VideoAdmin(AdminVideoMixin, AdminImageMixin, admin.ModelAdmin):
    list_display = ('title', 'category', 'is_active', 'sort')
    list_editable = ('is_active', 'sort')
    list_filter = ('is_active', 'category')
    fieldsets = (
        (None, {
            'fields': ('category', 'title', 'video_url', 'video_file', 'image', 'is_active',
                       'sort')},),
    )


admin.site.register(Item, VideoAdmin)

####################################################################################################
####################################################################################################