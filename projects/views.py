from django.shortcuts import render
from .models import post 
from django.views.generic import ListView, DetailView 

class projects_lst(ListView):
	model = post 
	template_name = 'projects/project.html'

class post_detail(DetailView):
	model = post 
	template_name = 'projects/full_detail.html'

