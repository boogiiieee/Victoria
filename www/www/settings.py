# -*- coding: utf-8 -*-

import os


def rel(*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)


SECRET_KEY = 'k6!rr7e=pvp^6c29f8hcfnmc%a$_=q2z*1km(_-ucf^c3_1@&3'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    #('GVA', 'GladkiyVA@gmail.com'),
    #('POA', 'poa.webaspect@gmail.com'),
    ('KVS', 'webaspect.test@gmail.com@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'victoria',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '5432',
    }
}

ALLOWED_HOSTS = ['127.0.0.1:8000', 'localhost:8000']

TIME_ZONE = 'Asia/Novosibirsk'
LANGUAGE_CODE = 'ru-ru'

SITE_ID = 1

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = rel('media')
MEDIA_URL = '/media/'

STATIC_ROOT = rel('static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'my_flatpages.middleware.FlatpageFallbackMiddleware',
    'configuration.middleware.ConfigurationMiddleware',
)

ROOT_URLCONF = 'www.urls'

#WSGI_APPLICATION = 'www.wsgi.application'

TEMPLATE_DIRS = (
    rel('..', 'admin_tools_ru', 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.sitemaps',

    'widget_tweaks',

    'victoria',
    'front_admin',
    'my_flatpages',
    'configuration',
    'simpleblocks',
    'copyright',
    'paginator',
    'article',
    'news',
    'contacts',
    'feedback',
    'map2gis',
    'questionanswer',
    'video',
    'videoplayer',

    'sorl.thumbnail',
    'annoying',
    #'django_cleanup',
    'robots',
    'ckeditor',
    'captcha',
    'south',
    'embed_video',
    'forums',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

CKEDITOR_UPLOAD_PATH = "ckeditor/uploads/"

CKEDITOR_CONFIGS = {
    'default': {

        'lang': 'ru',
        'toolbar_Custom': [
            ['Styles', 'Format', 'Font', 'FontSize', 'Bold', 'Italic', 'Underline', 'Strike',
             'SpellChecker', 'Undo', 'Redo'],
            ['Image', 'Flash', 'Table', 'HorizontalRule'],
            ['TextColor', 'BGColor'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote',
             'CreateDiv', '-',
             'JustifyLeft',
             'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-'], ['Link', 'Unlink', 'Anchor'],
            ['Source'],
        ],
        'toolbar': 'Custom',
    },

}

PAGINATE_BY = 10
ARTICLE_PAGINATE_BY = PAGINATE_BY
NEWS_PAGINATE_BY = PAGINATE_BY
QUESTIONANSWER_PAGINATE_BY = PAGINATE_BY

VIDEOPLAYER_DEFAULT_CONFIG = {
    'autostart': False, #True or False
    #'image': True, #url or False
    'start': 0, #Number
    'title': 'Title', #Text
    'description': 'description', #Text
    'controlbar': True, #True or False
    'duration': 57, #Number
    'volume': 80, #Number
    'width': 300, #Number
    'height': 250, #Number
    'aspectratio': "16:9",
    'events': {
        'onReady': None, #Text
        'onVolume': None, #Text
        'onError': None, #Text
        'onPlay': "onplay();", #Text
        'onPause': None, #Text
        'onSeek': None, #Text
        'onComplete': None, #Text
        'onTime': None, #Text
    }
}

VIDEO_EXTENSION = ('avi', 'mp4')

ROBOTS_SITEMAP_URLS = ['http://127.0.0.1:8000/sitemap.xml']
ROBOTS_SITEMAP_HOST = '127.0.0.1:8000'

CAPTCHA_NOISE_FUNCTIONS = ('captcha.helpers.noise_arcs',)

ADMIN_TOOLS_MENU = 'www.dashboard.CustomMenu'
ADMIN_TOOLS_INDEX_DASHBOARD = 'www.dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'www.dashboard.CustomAppIndexDashboard'
ADMIN_TOOLS_THEMING_CSS = 'admin_tools/css/theming_tomu.css'

DEFAULT_FROM_EMAIL = 'tester@web-aspect.ru'
EMAIL_HOST = 'smtp.locum.ru'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'tester@web-aspect.ru'
EMAIL_HOST_PASSWORD = 'iostream'
EMAIL_USE_TLS = True