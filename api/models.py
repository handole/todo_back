from django.db import models
from datetime import datetime

# Create your models here.
class Todo(models.Model):
	title = models.CharField(max_length=255, null=False)
	description = models.TextField()
	completed = models.BooleanField(default=False)

	def __str__(self):
		return "{} - {}".format(self.title, self.completed)
		

