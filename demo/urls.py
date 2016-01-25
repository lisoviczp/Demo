from django.conf.urls import url
from . import views

# Defining URLS
urlpatterns = [
	url(r'^send_message$', views.send_message, name='send_message'),
	url(r'^your_messages$', views.your_messages, name='your_messages'),

]