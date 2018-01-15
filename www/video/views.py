# -*- coding: utf-8 -*-

from django.views.generic import ListView
from django.conf import settings as conf

from video.models import Item


####################################################################################################
####################################################################################################


class VideoList(ListView):
    paginate_by = conf.PAGINATE_BY
    template_name = 'video/list.html'
    context_object_name = 'video_list'

    def get_queryset(self):
        return Item.activs.all()

    def get_context_data(self, **kwargs):
        context = super(VideoList, self).get_context_data(**kwargs)
        context.update({'active': 'video'})
        return context

####################################################################################################
####################################################################################################


