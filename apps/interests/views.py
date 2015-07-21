from django.http import HttpResponse, Http404
from django.shortcuts import render
from apps.interests.models import Interest, User
def index(request):
	#retreiving all of the users from the database
	users = User.objects.all()
	#packaging the data in a dictionary to pass to the template
	context = {'users': users}
	#send the response to the html page to be viewed with the data included
	return render(request, 'interests/index.html', context)
def show(request, id):
	#users based on the user id passed through the url
	user = User.objects.get(id=id)
	#package the data in a dictionary to pass to the template
	content={'user': user}
	return render(request, 'interests/show.html', content)
# Create your views here.
