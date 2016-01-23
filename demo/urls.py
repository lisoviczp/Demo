from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
	url(r'^send_message$', views.send_message, name='send_message'),
	url(r'^your_messages$', views.your_messages, name='your_messages'),

]