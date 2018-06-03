from django.shortcuts import render
from .models import about 

def about_post(request):
	post = about.objects.all()
	context = {'post':post}
	return render(request, 'index.html', context)

