from django.shortcuts import render

def coc(request):
	return render(request, 'coc/coc.html')