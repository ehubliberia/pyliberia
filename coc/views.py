from django.shortcuts import render
from .models import code_of_conduct

def coc(request):
	code = code_of_conduct.objects.all()
	context = {'code':code}
	return render(request, 'coc/coc.html', context)