from django.shortcuts import render 
from about.models import about 
from projects.models import project
from constitution.models import const
from coc.models import coc

def about_post(request):
	post = about.objects.all()
	coc_lst = coc.objects.all()
	constit = const.objects.all()
	proj = project.objects.all()
	context = {'post':post, 'proj':proj, 'coc_lst':coc_lst, 'constit':constit}
	return render(request, 'index.html', context)

