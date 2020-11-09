from django.db import models
from django.contrib.auth.models import User

class Plan(models.Model):
    name = models.CharField(max_length=20)
    review = models.TextField(max_length=100, default='SOME STRING')
    description = models.TextField(max_length=1000)
    price = models.IntegerField(default=0)