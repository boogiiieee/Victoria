# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, Http404
from django.template import Context
from django.template.loader import get_template
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.core.mail import mail_managers
from django.utils.translation import ugettext_lazy as _

from questionanswer.models import Subject, Item
from questionanswer.forms import QuestionAnswerForm
from questionanswer.conf import settings as conf

####################################################################################################
####################################################################################################


class QuestionList(FormMixin, ListView):
    paginate_by = conf.PAGINATE_BY
    form_class = QuestionAnswerForm
    success_url = reverse_lazy('question_url')
    template_name = 'questions/question.html'
    context_object_name = 'question_list'
    subject = Subject.activs.all()

    def get_queryset(self):
        return Item.activs.all()

    def get_context_data(self, **kwargs):
        context = super(QuestionList, self).get_context_data(**kwargs)
        context.update(dict(active='question', subject='subject'))
        return context

    def get_paginate_obect_list(self):
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()

        if not allow_empty:
            if (self.get_paginate_by(self.object_list) is not None
                and hasattr(self.object_list, 'exists')):
                is_empty = not self.object_list.exists()
            else:
                is_empty = len(self.object_list) == 0
            if is_empty:
                raise Http404(_("Empty list and '%(class_name)s.allow_empty' is False.")
                              % {'class_name': self.__class__.__name__})
        return self.object_list

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(
            self.get_context_data(object_list=self.get_paginate_obect_list(), form=form)
        )

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        q = form.cleaned_data
        q.pop('captcha', None)
        item = Item.objects.create(**q)

        domain = Site.objects.get_current().domain

        subject = u'Новый вопрос на сайте %s' % domain

        t = get_template('mail/question.html')
        message = t.render(Context({'item': item, 'domain': domain}))

        mail_managers(subject, message, html_message=message)

        messages.add_message(self.request, messages.INFO, u'Спасибо! Ваш вопрос отправлен!')
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(object_list=self.get_paginate_obect_list(), form=form)
        )

        ####################################################################################################
        ####################################################################################################