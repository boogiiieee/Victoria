# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.views.generic.edit import FormView
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.core.mail import mail_managers

from feedback.models import FeedBackItem
from feedback.forms import FeedBackForm

################################################################################################################
################################################################################################################


class FeedbackView(FormView):
    form_class = FeedBackForm
    success_url = reverse_lazy('contacts_url')
    template_name = 'flatpages/contacts.html'

    def get_context_data(self, **kwargs):
        context = super(FeedbackView, self).get_context_data(**kwargs)
        context.update({'active': 'contacts', })
        return context

    def form_valid(self, form):
        q = form.cleaned_data
        q.pop('captcha', None)
        item = FeedBackItem.objects.create(**q)

        domain = Site.objects.get_current().domain

        subject = u'Новое сообщение на сайте %s' % domain

        t = get_template('mail/feedback.html')
        message = t.render(Context({'item': item, 'domain': domain}))

        mail_managers(subject, message, html_message=message)

        messages.add_message(self.request, messages.INFO, u'Спасибо! Ваше сообщение отправлено!')
        return HttpResponseRedirect(self.get_success_url())

        ################################################################################################################
        ################################################################################################################