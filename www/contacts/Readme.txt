Приложение для вывода контактной информации  в шаблоне.

INSTALLED_APPS = (
	...
	'contacts',
	...
)
{% load contacts_tags %}
{% get_contact_info 'var_name' %}