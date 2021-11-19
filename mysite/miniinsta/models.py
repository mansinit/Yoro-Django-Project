from django.db import models
from django.conf import settings
import os

def upload_to(category,filename):
   return os.path.join(category,filename)

class Pictures(models.Model):
   image = models.ImageField(upload_to='', null=True,blank=True)

class Albums(models.Model):
   album = models.TextField( null=True,blank=True)
