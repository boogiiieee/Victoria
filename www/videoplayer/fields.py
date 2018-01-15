# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings

####################################################################################################
####################################################################################################


def validate_video(value):
    """
    проверка допустимых расширений видеофайлов
    расширения задаются в settings
    """
    ext = value.name.split('.')[-1]
    if not ext in settings.VIDEO_EXTENSION:
        raise ValidationError(u'Некорректный тип видео файла.')


class VideoField(models.FileField):
    """
    создаем поле VideoField для загрузки видеофайлов
    добавляем новое поле для South
    """

    def south_field_triple(self):
        from south.modelsinspector import introspector

        cls_name = '%s.%s' % (self.__class__.__module__, self.__class__.__name__)
        args, kwargs = introspector(self)
        return cls_name, args, kwargs

    default_validators = [validate_video]

####################################################################################################
####################################################################################################