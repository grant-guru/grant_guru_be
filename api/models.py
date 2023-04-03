from django.db import models
from django.contrib.postgres import fields

class User(models.Model):
  first_name = models.TextField()
  last_name = models.TextField()
  
class Grant(models.Model):
  title = models.TextField()
  organization = models.TextField()
  description = models.TextField()
  amount = models.IntegerField()
  deadline = models.DateField()
  education = models.TextField()
  state = models.TextField()
  ethnicity = fields.ArrayField(models.TextField(), default=list)
  women = models.BooleanField()
  lgbt = models.BooleanField()
  veteran = models.BooleanField()
  immigrant = models.BooleanField()
  url = models.URLField()
  image_url = models.URLField()
  users = models.ManyToManyField(User, blank=True)