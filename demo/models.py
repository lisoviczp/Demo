from django.db import models

# Create your models here.

from django.db import models
from swampdragon.models import SelfPublishModel
from .serializers import NotificationSerializer
from django.contrib.auth.models import User
from django.conf import settings

DEFAULT_USER_ID=2

class User(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	email = models.CharField(max_length=50)

	def __str__(self):
		return str(self.username) or '' 

	def __unicode__(self):
		return unicode(self.username) or u''

class Notification(SelfPublishModel, models.Model):
    serializer_class = NotificationSerializer
    message = models.TextField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE,default=DEFAULT_USER_ID, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='receiving_user')
    sending_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sending_user', default = DEFAULT_USER_ID)

    def __str__(self):
    	return_message = "Message: " + str(self.message) + "\n" 
    	return_message += "User: " + str(self.user) + "\n" or ''
    	return return_message
    	# return "Message: " + str(self.message) + "\n" 

    def __unicode(self):
    	return unicode(self.message) or u''
