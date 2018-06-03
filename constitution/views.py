from django.shortcuts import render

def const(request):
	return render(request, 'constitution/const.html')