from django.db import models

# Create your models here.
class Finch(models.Model): 
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.CharField(max_length=250)
  age = models.IntegerField()
  
  def _str_(self):
    return self.name