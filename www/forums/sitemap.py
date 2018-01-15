# -*- coding: utf-8 -*-

from django.contrib.sitemaps import Sitemap

from forums.models import Forum, Topic

####################################################################################################
####################################################################################################


#Для карты сайта
class ForumSitemap(Sitemap):
    def items(self):
        return Forum.objects.all()

    def location(self, obj):
        return obj.get_absolute_url()


class TopicSitemap(Sitemap):
    def items(self):
        return Topic.objects.all()

    def location(self, obj):
        return obj.get_absolute_url()



####################################################################################################
####################################################################################################