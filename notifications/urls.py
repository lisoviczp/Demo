"""notifications URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
""" 
# orig
# from django.conf.urls import include, url
# from django.contrib import admin

# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
# ]

from demo import views
from django.conf.urls import patterns, include, url
from django.contrib import admin
from demo.views import Notifications
from demo.views import Users

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', Notifications.as_view(), name='home'),
    url(r'^home/$', Notifications.as_view(), name='home'),
	url(r'^users/$', Users.as_view(), name='home'),
	url(r'^demo/', include('demo.urls')),
	url(r'^home/send_message$', views.send_message, name='send_message'),
    url(r'^new_message/(?P<user_id>\d+)$', views.new_message_form, name='new_message_form'),
    url(r'^home/your_messages/$', views.your_messages, name='your_messages'),
	url(r'^admin/', include(admin.site.urls)),
)
