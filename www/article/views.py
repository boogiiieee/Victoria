# -*- coding: utf-8 -*-

from django.views.generic import ListView, DetailView

from article.models import Item
from article.conf import settings as conf

####################################################################################################
####################################################################################################


class ArticleMixin(object):
    def get_queryset(self):
        return Item.activs.all()

    def get_context_data(self, **kwargs):
        context = super(ArticleMixin, self).get_context_data(**kwargs)
        context.update({'active': 'article'})
        return context

####################################################################################################
####################################################################################################


class ArticleList(ArticleMixin, ListView):
    paginate_by = conf.PAGINATE_BY
    template_name = 'article/list.html'
    context_object_name = 'article_list'

####################################################################################################
####################################################################################################


class ArticleView(ArticleMixin, DetailView):
    template_name = 'article/article.html'

####################################################################################################
####################################################################################################