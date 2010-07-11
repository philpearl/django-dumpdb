from datetime import datetime

from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateTimeField(default=datetime.now)
    parent = models.ForeignKey('self', null=True)

class Family(models.Model):
    members = models.ManyToManyField(Person)
