# -*- coding: utf-8 -*-

from django.contrib import admin
from django.conf import settings

from contacts.models import Contacts, Phone, Email, Skype, Social

####################################################################################################
####################################################################################################


class PhoneInline(admin.StackedInline):
    fields = ('phone', 'desc_phone', 'is_active', 'sort')
    model = Phone
    extra = 0


class EmailInline(admin.StackedInline):
    fields = ('email', 'desc_email', 'is_active', 'sort')
    model = Email
    extra = 0


class SkypeInline(admin.StackedInline):
    fields = ('skype', 'desc_skype', 'is_active', 'sort')
    model = Skype
    extra = 0


class SocialInline(admin.StackedInline):
    fields = ('title', 'social_url', 'icon', 'is_active', 'sort')
    model = Social
    extra = 0


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('title', 'site', 'alt_adress', 'work_time')
    inlines = [PhoneInline, EmailInline, SkypeInline, SocialInline, ]
    fieldsets = (
        (None, {'fields':
                    ('title', 'work_time', 'site', 'desc_site', 'adress', 'alt_adress',
                     'desc_adress')
                }
        ),
    )

    def has_add_permission(self, *args, **kwargs):
        """
        Запрещаем добавлять новые экземпляры Contacts при DEBUG=False
        """
        if settings.DEBUG:
            return True
        else:
            return False

    def has_delete_permission(self, *args, **kwargs):
        """
        Запрещаем удалять экземпляры Contacts при DEBUG=False
        """
        if settings.DEBUG:
            return True
        else:
            return False


admin.site.register(Contacts, ContactsAdmin)