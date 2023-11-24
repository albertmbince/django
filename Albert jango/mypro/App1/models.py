from django.db import models
class student(models.Model):
    rollno=models.IntegerField()
    name=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    def __str__(self):
       return self.name
   
        

# Create your models here.
