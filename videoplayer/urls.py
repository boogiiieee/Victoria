from django.conf.urls.defaults import *

urlpatterns = patterns('videoplayer.views',
	url(r'^(?P<lesson_id>[0-9]{1,4})/(?P<url>.+)/$', 'add_video_frame'),
)