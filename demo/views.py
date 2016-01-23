from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import ListView
from .models import Notification
from django.contrib.auth.models import User


class Notifications(ListView):
	model = Notification
	template_name = 'home.html'
	# users = forms.ModelChoiceField(queryset=Users.objects.all().order_by('username'))

	def get_queryset(self):
		return self.model.objects.order_by('-pk')[:25]

def your_messages(request):
	current_user=request.user
	context=RequestContext(request)
	context_dict = {}
	return render_to_response('your_messages.html', context_dict, context)


def send_message(request):
	current_user=request.user
	context=RequestContext(request)
	context_dict = {}

	print("CURRENT USER: ")
	print(current_user)


	if request.POST:
		new_message=request.POST.get('notification')
		new_user=str(request.POST.get('user'))
		print(new_user)
		print(User.objects.all())

		uu=User.objects.get(username=new_user)
		print("NEWUSER: " + str(uu))

		print(new_message)
		n=Notification(message=new_message, user=uu)
		n.save()
		# print(n)
		# return HttpResponse('200')
		return render_to_response('home.html', context_dict, context)
		# return HttpResponseRedirect('/home/')

	# return render_to_response('home.html', context_dict, context)
	# return HttpResponseRedirect('/')
	# return True



class Users(ListView):
	model = User
	template_name = 'users.html'

	def get_queryset(self):
		return self.model.objects.order_by('-pk')[:25]