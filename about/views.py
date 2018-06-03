from django.shortcuts import render
from .models import about 

def about_post(request):
	post = about.objects.all()
	coc_lst = coc.objects.all()
	constit = const.objects.all()
	proj = project.objects.all()
	context = {'post':post, 'proj':proj, 'coc_lst':coc_lst, 'constit':constit}
	return render(request, 'index.html', context)

