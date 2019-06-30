from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
	name = models.CharField(max_length=250)
	short = models.CharField(max_length=250, default ='fillme')
	icon = models.CharField(max_length=250)

class Question(models.Model):
    text = models.CharField(max_length=1000)
    company = models.CharField(max_length=250)
    date = models.IntegerField()
    belongs_to = models.ForeignKey(Job, related_name='question', on_delete='SET_NULL', null=True)
    