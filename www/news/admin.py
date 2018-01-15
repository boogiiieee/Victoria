# -*- coding: utf-8 -*-

from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin

from news.models import Item

####################################################################################################
####################################################################################################

class NewsAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'is_active', 'sort')
    search_fields = ('title', 'slug')
    list_filter = ('is_active', 'created_at')
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ('is_active', 'sort')
    fieldsets = (
        (None, {'fields': ('title', 'slug', 'text', 'image', 'is_active', 'sort')},),
        (u'Мета-теги', {'classes': ('collapse',), 'fields': ('description', 'keywords')}),
    )


admin.site.register(Item, NewsAdmin)

####################################################################################################
####################################################################################################