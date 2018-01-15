# -*- coding: utf-8 -*-

from django.conf.urls import *

from feedback.views import FeedbackView

urlpatterns = patterns('feedback.views',
    url(r'^$', FeedbackView.as_view(), name='contacts_url'),
)