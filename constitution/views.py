from django.shortcuts import render
from .models import constitution

def const(request):
	consti = constitution.objects.all()
	context = {'consti':consti}
	return render(request, 'constitution/const.html', context)