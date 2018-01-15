# -*- coding: utf-8 -*-

from django.conf.urls import *

from video.views import VideoList

urlpatterns = patterns('video.views',
                       url(r'^$', VideoList.as_view(), name='video_list_url'),
)
