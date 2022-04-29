from unicodedata import name
from django.db import models
class contact_us(models.Model):
    yourname=models.CharField(max_length=200)
    youremail=models.CharField(max_length=200)
    yourphone=models.CharField(max_length=200)
    yourproblem=models.CharField(max_length=200)
class book(models.Model):
    State=models.CharField(max_length=200)
    Places=models.CharField(max_length=200)
    Date=models.CharField(max_length=200)
    Enddate=models.CharField(max_length=200,null=True)