Приложение для вывода видео в шаблоне.

Вывод   - 1. ссылка с YouTube
		  2. видеофайл формата avi, mp4

Работает в паре с приложениями videoplayer и embed_video

INSTALLED_APPS = (
	...
	'video',
	...
)

VIDEO_EXTENSION = ('avi', 'mp4')

в шаблоне -  {{ video_list }}