import json
from unicodedata import category
from django.db import models
from rest_framework.validators import UniqueValidator

from authenticator.models import User

# Create your models here.
class Categories(models.Model):
  nm_category = models.CharField(max_length=32)
  color = models.CharField(max_length=7,default="#ffffff")
  user = models.ForeignKey(User,null=True,blank=False,on_delete=models.CASCADE)

  def __str__(self):
    obj = {
      'id': self.id,
      'nm_category': self.nm_category,
      'user': self.user.id,
      'color': self.color,
    }
    return json.dumps(obj)
  
class Todo(models.Model):
  PRIORITY_CHOICES = ((0,'Muito Importante'),(1,'Importante'),(2,'Normal'),(3,'Pouco Importante'))
  title = models.CharField(max_length=24,null=False,blank=False)
  description = models.CharField(max_length=140,null=True,blank=True)
  deadline = models.DateField(null=True,blank=True)
  category = models.ForeignKey(Categories,on_delete=models.CASCADE)
  priority = models.IntegerField(choices=PRIORITY_CHOICES)
  user = models.ForeignKey(User,null=True,blank=False,on_delete=models.CASCADE)

  # def __str__(self): 
  #   obj = {}
  #   for (key,value) in self:
  #     obj[key] = value
      
  #   return json.dumps(obj)