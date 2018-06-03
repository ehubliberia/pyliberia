from django.urls import path
from . import views  

urlpatterns = [
	path('', views.coc, name='coc'),
]