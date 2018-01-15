# -*- coding: utf-8 -*-

from django.views.generic import ListView, DetailView

from news.models import Item
from news.conf import settings as conf

####################################################################################################
####################################################################################################


class NewsMixin(object):
    def get_queryset(self):
        return Item.activs.all()

    def get_context_data(self, **kwargs):
        context = super(NewsMixin, self).get_context_data(**kwargs)
        context.update({'active': 'news'})
        return context

####################################################################################################
####################################################################################################


class NewsList(NewsMixin, ListView):
    paginate_by = conf.PAGINATE_BY
    template_name = 'news/list.html'
    context_object_name = 'news_list'

####################################################################################################
####################################################################################################


class NewsView(NewsMixin, DetailView):
    template_name = 'news/news.html'

####################################################################################################
####################################################################################################