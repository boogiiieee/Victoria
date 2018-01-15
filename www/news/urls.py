# -*- coding: utf-8 -*-

from django.conf.urls import *

from news.views import NewsList, NewsView

urlpatterns = patterns('news.views',
    url(r'^$', NewsList.as_view(), name='news_list_url'),
    url(r'^(?P<slug>[-_\w]+)/$', NewsView.as_view(), name='news_url'),
)