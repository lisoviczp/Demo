from django.db import models

# Create your models here.

from django.db import models
from swampdragon.models import SelfPublishModel
from .serializers import NotificationSerializer
from django.contrib.auth.models import User
from django.conf import settings

# Set a default 'sending_user' because I added that attribute in later
DEFAULT_USER_ID=2

# Generic User model taken from Django's auth.models
class User(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	email = models.CharField(max_length=50)

	def __str__(self):
		return str(self.username) or '' 

	def __unicode__(self):
		return unicode(self.username) or u''

# Notification model with user (recipient) and sending_user (sender) as foreign keys 
# Using Serializers.py to translate/publish the model's message data
class Notification(SelfPublishModel, models.Model):
    serializer_class = NotificationSerializer
    message = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='receiving_user')
    sending_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sending_user', default = DEFAULT_USER_ID)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	return_message = "Message: " + str(self.message) + "\n" 
        return_message += "Receiving User: " + str(self.user) + "\n" or ''
    	return_message += "Sending User: " + str(self.sending_user) + "\n" or ''
    	return return_message

    def __unicode(self):
    	return unicode(self.message) or u''
