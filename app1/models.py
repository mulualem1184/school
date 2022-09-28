from django.db import models
from django.core.exceptions import *
import os
class slidepicture(models.Model):
        picture = models.ImageField(("this is an image for the product"), )
    
        class Meta:
              db_table= "slidepicture"
       
class barpicture(models.Model):
        picture = models.ImageField(("this is an image for bar"), )
    
        class Meta:
              db_table= "barpicture"
       
class video(models.Model):
        
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)
class modelteacher(models.Model):
        first_name=models.CharField(max_length = 50)
        second_name=models.CharField(max_length=50)
        department=models.CharField(max_length=50)
        picture = models.ImageField(("this is an image for the product"), )
    
        class Meta:
              db_table= "first_name"

class partner(models.Model):
       
        name= models.CharField(max_length= 100)
        picture = models.ImageField(("this is an image for bar"), )
        hlink= models.CharField(max_length=100)

    
        class Meta:
              db_table= "name"