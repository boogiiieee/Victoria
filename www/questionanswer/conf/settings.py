# -*- coding: utf-8 -*-

from django.conf import settings

PAGINATE_BY = getattr(settings, 'QUESTIONANSWER_PAGINATE_BY', 2)