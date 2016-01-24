from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import ListView
from .models import Notification
from django.contrib.auth.models import User
from django.db.models import Q
from django import forms

class Users(ListView):
	model = User
	template_name = 'users.html'

	def get_queryset(self):
		return self.model.objects.order_by('-pk')[:25]

class Notifications(ListView):
	model = Notification
	template_name = 'home.html'
	users = forms.ModelChoiceField(queryset=User.objects.all().order_by('username'))

	def get_queryset(self):
		return self.model.objects.order_by('-pk')[:25]


def your_messages(request):
	current_user=request.user
	context=RequestContext(request)
	context_dict = {}

	your_messages = Notification.objects.filter(user=current_user)
	context_dict['your_messages'] = your_messages

	return render_to_response('your_messages.html', context_dict, context)

def new_message_form(request,user_id):
	current_user=request.user
	other_user = User.objects.get(id=user_id)
	print(other_user)
	print(current_user)
	context=RequestContext(request)
	context_dict = {}

	other_user = User.objects.get(id=user_id)

	# Here we're getting the "relevant messages" for these users, ie all messages where only these users are involved
	relevant_messages = Notification.objects.filter(Q(user=current_user,sending_user=other_user) | Q(user=other_user,sending_user=current_user)).order_by('-created')

	context_dict['other_user'] = other_user
	context_dict['relevant_messages'] = relevant_messages
	return render_to_response('new_message_form.html', context_dict, context)


def send_message(request):
	current_user=request.user
	context=RequestContext(request)
	context_dict = {}

	if request.POST:
		new_message=request.POST.get('notification')
		new_user=str(request.POST.get('user'))
		# print(User.objects.all())

		uu=User.objects.get(username=new_user)
		
		print("Sender: " + str(current_user))
		print("Recipent: " + str(uu))
		print("Message: " + new_message)

		n=Notification(message=new_message, user=uu, sending_user=current_user)
		n.save()
		# return HttpResponse('200')
		# return render_to_response('home.html', context_dict, context)



