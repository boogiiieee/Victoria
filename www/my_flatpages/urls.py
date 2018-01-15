from django.conf.urls import *

urlpatterns = patterns('my_flatpages.views',
    (r'^(?P<url>.*)$', 'flatpage'),
)
