from django.db import models

class coc(models.Model):
	Coc_Title = models.CharField(max_length=150)
	Coc_Body = models.TextField()

	def __str__(self):
		return self.Coc_Title