# -*- coding: utf-8 -*-

from django.conf.urls import *

from questionanswer.views import QuestionList

urlpatterns = patterns('questionanswer.views',
    url(r'^$', QuestionList.as_view(), name='question_url'),
)