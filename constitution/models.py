from django.db import models

class const(models.Model):
	Constitution_Title = models.CharField(max_length=150)
	Constitution_Body = models.TextField()

	def __str__(self):
		return self.Constitution_Title

class constitution(models.Model):
	Title = models.CharField(max_length=150)
	Body = models.TextField()

	def __str__(self):
		return self.Title 