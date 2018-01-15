# -*- coding: utf-8 -*-

from django.contrib import admin

from feedback.models import FeedBackItem

####################################################################################################
####################################################################################################


class FeedBackItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    list_filter = ('created_at',)
    fieldsets = (
        (None, {'fields': ('name', 'email', 'phone', 'msg')},),
    )


admin.site.register(FeedBackItem, FeedBackItemAdmin)

####################################################################################################
####################################################################################################