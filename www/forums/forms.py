# -*- coding: utf-8 -*-
from django import forms


class TopicCreateForm(forms.Form):
    topic = forms.CharField(label=u"Топик", min_length=3)
    message = forms.CharField(label=u"Сообщение", min_length=3, widget=forms.Textarea())


class PostCreateForm(forms.Form):
    message = forms.CharField(label=u"Сообщение", min_length=3, widget=forms.Textarea())
