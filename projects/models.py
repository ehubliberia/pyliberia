from django.db import models

class post(models.Model):
	Title = models.CharField(max_length=150)
	Date = models.DateField(auto_now_add=True)
	Event_Start = models.DateTimeField()
	Event_End = models.DateTimeField()
	Body = models.TextField()

	def __str__(self):
		return self.Title 

class project(models.Model):
	Project_Title = models.CharField(max_length=150)
	Project_Body = models.TextField()

	def __str__(self):
		return self.Project_Title
