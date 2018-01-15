# -*- coding: utf-8 -*-

from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin

from article.models import Item

####################################################################################################
####################################################################################################


class ArticleAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_active', 'sort')
    search_fields = ('title',)
    list_filter = ('is_active', 'created_at')
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ('is_active', 'sort')
    fieldsets = (
        (None, {'fields': ('title', 'slug', 'text', 'image', 'is_active', 'sort')},),
        (u'Мета-теги', {'classes': ('collapse',), 'fields': ('description', 'keywords')}),
    )

admin.site.register(Item, ArticleAdmin)

####################################################################################################
####################################################################################################