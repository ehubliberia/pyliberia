from django.urls import path 
from . import views 

urlpatterns = [
	path('', views.projects_lst.as_view(), name='projects'),
	path('fulldetail/<int:pk>/', views.post_detail.as_view(), name='full_post'), 
]