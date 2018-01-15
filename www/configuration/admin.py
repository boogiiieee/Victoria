# -*- coding: utf-8 -*-

from django.contrib import admin

from configuration.models import ConfigModel
from configuration.forms import ConfigForm

####################################################################################################
####################################################################################################


class ConfigModelAdmin(admin.ModelAdmin):
    form = ConfigForm
    fieldsets = (
        (None, {'fields': ('title', 'code_phone', 'phone', 'email', 'adress')}),
    )

    def has_add_permission(self, *args, **kwargs):
        return False

    def has_delete_permission(self, *args, **kwargs):
        return False

admin.site.register(ConfigModel, ConfigModelAdmin)

####################################################################################################
####################################################################################################