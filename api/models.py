from django.db import models
from django.contrib.postgres import fields

class User(models.Model):
  first_name = models.TextField()
  last_name = models.TextField()
  
class Grant(models.Model):
  title = models.TextField()
  organization = models.TextField()
  amount = models.IntegerField()
  description = models.TextField()
  deadline = models.DateField()
  education = models.TextField()
  state = models.TextField()
  women = models.BooleanField()
  lgbt = models.BooleanField()
  ethnicity = fields.ArrayField(models.TextField(), default=list)
  veteran = models.BooleanField()
  immigrant = models.BooleanField()
  url = models.URLField()
  image_url = models.URLField()
  users = models.ManyToManyField(User, blank=True)