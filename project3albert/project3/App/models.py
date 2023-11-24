from django.db import models
class student(models.Model):
    rollno=models.IntegerField(max_length=25)
    name=models.CharField(max_length=20)
    place=models.CharField(max_length=25)

# Create your models here.
