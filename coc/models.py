from django.db import models

class coc(models.Model):
	Coc_Title = models.CharField(max_length=150)
	Coc_Body = models.TextField()

	def __str__(self):
		return self.Coc_Title

class code_of_conduct(models.Model):
	Title = models.CharField(max_length=150)
	Body = models.TextField()

	def __str__(self):
		return self.Title 