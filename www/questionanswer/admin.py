# -*- coding: utf-8 -*-

from django.contrib import admin

from questionanswer.models import Subject, Item

####################################################################################################
####################################################################################################


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'sort')
    list_filter = ('is_active',)
    list_editable = ('is_active', 'sort')
    fieldsets = (
        (None, {'fields': ('title', 'is_active', 'sort')},),
    )


admin.site.register(Subject, SubjectAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'phone', 'date_question', 'is_active', 'sort')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('subject', 'is_active', 'date_question')
    list_editable = ('is_active', 'sort')


admin.site.register(Item, ItemAdmin)

####################################################################################################
####################################################################################################