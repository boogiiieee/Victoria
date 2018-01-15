# coding=utf-8

from django import forms
from django.contrib import admin
#from django.contrib.flatpages.models import FlatPage as oldFlatPage
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from my_flatpages.models import FlatPage

####################################################################################################
####################################################################################################


class FlatpageForm(forms.ModelForm):
    url = forms.RegexField(label=_("URL"), max_length=100, regex=r'^[-\w/\.~]+$',
                           help_text=_("Example: '/about/contact/'. Make sure to have leading"
                                       " and trailing slashes."),
                           error_message=_("This value must contain only letters, numbers,"
                                           " dots, underscores, dashes, slashes or tildes."))

    class Meta:
        model = FlatPage

####################################################################################################
####################################################################################################


class FlatPageAdmin(admin.ModelAdmin):
    form = FlatpageForm
    """
    при DEBUG=True показываем скрытые поля настроек
    """
    def __init__(self, *args, **kwargs):
        super(FlatPageAdmin, self).__init__(*args, **kwargs)

        self.fieldsets = [
            (None, {'fields': ('url', 'title', 'content', 'sites')},),
            (_('Meta tags'), {'classes': ('collapse',), 'fields': ('description', 'keywords')}),
        ]

        if settings.DEBUG:
            self.fieldsets += [
                (_('Advanced options'), {'classes': ('collapse',), 'fields': ('enable_comments',
                                                                              'registration_required',
                                                                              'template_name')}),
            ]

    list_display = ('title', 'url')
    search_fields = ('title', 'url')

#admin.site.unregister(oldFlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

####################################################################################################
####################################################################################################