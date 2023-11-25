from django.db import models
class book(models.Model):
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=25)
    image=models.CharField(max_length=225)
# Create your models here.
