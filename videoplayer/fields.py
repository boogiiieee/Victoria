# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings

def validate_video(value):
	ext = value.name.split('.')[-1]
	if not ext in settings.VIDEO_EXTENSION:
		raise ValidationError(u'Некорректный тип видео файла.')
		
class VideoField(models.FileField):
	default_validators = [validate_video]

