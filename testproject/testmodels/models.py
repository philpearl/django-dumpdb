from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateTimeField()
    parent = models.ForeignKey('self')

class Family(models.Model):
    members = models.ManyToManyField(Person)
