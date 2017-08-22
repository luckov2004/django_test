from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
	objects = QuestionManager()
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateField()
	rating =models. int(10)
	author = models.ForeignKey(User, on_delete=models.SET_NULL)
	likes = models.ManyToManyField(User)

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateField()
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.SET_NULL)

class QuestionManager(models.Manager):
	def new():
		pass
	def popular():
		pass

