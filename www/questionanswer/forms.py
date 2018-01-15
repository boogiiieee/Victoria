# -*- coding: utf-8 -*-

from django import forms
from captcha.fields import CaptchaField, CaptchaTextInput
from captcha.conf import settings
import cgi
import re
from django.utils.translation import ugettext

from questionanswer.models import Item, Subject

####################################################################################################
####################################################################################################


class NewCaptchaImgOutput(CaptchaTextInput):
    def render(self, name, value, attrs=None):
        """
        Переопределение стандартного вывода изображения капчи для лучшего управления во
        фронтенде.
        """
        empty_block = '<div class="span1"></div>'
        self.fetch_captcha_store(name, value, attrs)

        self.image_and_audio = '<img src="%s" alt="captcha" class="captcha span3" />%s' \
                               % (self.image_url(), empty_block)
        if settings.CAPTCHA_FLITE_PATH:
            self.image_and_audio = '<a href="%s" title="%s">%s</a>' % (self.audio_url(),
                                                                       ugettext(
                                                                           'Play CAPTCHA as '
                                                                           'audio file'),
                                                                       self.image_and_audio)
        return super(CaptchaTextInput, self).render(name, self._value, attrs=attrs)


class QuestionAnswerForm(forms.ModelForm):
    captcha = CaptchaField(widget=NewCaptchaImgOutput(
        attrs={'placeholder': 'Код защиты', 'class': 'span8', 'required': True}))
    question = forms.CharField(max_length=1000, widget=forms.Textarea(
        attrs={'placeholder': "Ваш вопрос", 'class': 'span12', 'rows': '5', 'required': True}))
    subject = forms.ModelChoiceField(queryset=Subject.activs.all(), empty_label=u'Тема вопроса',
                                     widget=forms.Select(attrs={'class': 'span12 subject'}))

    class Meta:
        model = Item
        fields = ('name', 'email', 'phone', 'captcha', 'subject', 'question')
        widgets = dict(name=forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'span10 name',
                                                   'required': True}),
                       email=forms.TextInput(attrs={'placeholder': 'E-mail', 'class': 'span10 '
                                                                                      'email'}),
                       phone=forms.TextInput(attrs={'placeholder': "Телефон", 'class': 'span10 '
                                                                                       'phone'}))

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError(u'Слишком короткое ФИО - не меньше 3 символов')
        return name

    def clean_email(self):
        email = self.cleaned_data['email']
        if email:
            r = re.compile(
                '^[0-9a-zA-Z]+[-\._0-9a-zA-Z]*@[0-9a-zA-Z]+'
                '[-\._^0-9a-zA-Z]*[0-9a-zA-Z]+[\.]{1}[a-zA-Z]{2,6}$')
            if not r.findall(email):
                raise forms.ValidationError(u'Некорректный E-mail')
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if phone:
            r = re.compile('^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{6,10}$')
            if not r.findall(phone):
                raise forms.ValidationError(u'Некорректный номер телефона')
        return phone

    def clean_question(self):
        question = self.cleaned_data['question']
        question = cgi.escape(question)
        if len(question) < 10:
            raise forms.ValidationError(u'Слишком короткий вопрос - не меньше 10 символов')
        return question

        ####################################################################################################
        ####################################################################################################