from django.db import models

class about(models.Model):
	About_Title = models.CharField(max_length=150)
	Body = models.TextField()

	def __str__(self):
		return self.About_Title