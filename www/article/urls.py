# -*- coding: utf-8 -*-

from django.conf.urls import *

from article.views import ArticleList, ArticleView

urlpatterns = patterns('article.views',
                       url(r'^$', ArticleList.as_view(), name='article_list_url'),
                       url(r'^(?P<slug>[-_\w]+)/$', ArticleView.as_view(), name='article_url'),
)