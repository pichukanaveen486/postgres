from django.db import models

# Create your models here.
class Topic(models.Model):
    tn=models.CharField(primary_key=True,max_length=100)



class webpage(models.Model):
    tn=models.ForeignKey(Topic,max_length=100,on_delete=models.CASCADE) 
    name=models.CharField(max_length=100) 