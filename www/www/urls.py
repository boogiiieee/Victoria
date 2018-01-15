# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib.sitemaps import FlatPageSitemap
from django.conf import settings

from django.contrib import admin

admin.autodiscover()

from news.sitemap import NewsSitemap
from article.sitemap import ArticleSitemap
from forums.sitemap import ForumSitemap, TopicSitemap

sitemaps = {
    'flatpages': FlatPageSitemap,
    'news': NewsSitemap,
    'article': ArticleSitemap,
    'forums': ForumSitemap,
    'topic': TopicSitemap,
}

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^admin_tools/', include('admin_tools.urls')),

                       url(r'^ckeditor/', include('ckeditor.urls')),
                       url(r'^captcha/', include('captcha.urls')),

                       url(r'^article/', include('article.urls')),
                       url(r'^contacts/', include('feedback.urls')),
                       url(r'^question/', include('questionanswer.urls')),
                       url(r'^news/', include('news.urls')),
                       url(r'^video/', include('video.urls')),
                       url(r'^forums/', include('forums.urls',  namespace='forums')),

                       url(r'^robots\.txt$', include('robots.urls')),
                       url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
                           {'sitemaps': sitemaps}),

                       url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.STATIC_ROOT}),
                       url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.MEDIA_ROOT}),
)
