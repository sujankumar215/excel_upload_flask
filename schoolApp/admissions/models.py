from django.db import models
from django.urls import  reverse

# Create your models here.

class Student(models.Model):
    name= models.CharField(max_length=50)
    fathername = models.CharField(max_length=50)
    classname = models.IntegerField()
    contact = models.CharField(max_length=50)



class Teacher(models.Model):
    name= models.CharField(max_length=50)
    exp = models.IntegerField()
    subject= models.CharField(max_length=50)
    contact = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse("listteachers")
    