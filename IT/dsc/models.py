from django.db import models
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=10)
    roll = models.IntegerField()
    course= models.CharField(max_length=10)
