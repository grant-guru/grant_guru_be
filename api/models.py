from django.db import models
from django.contrib.postgres import fields


class Grant(models.Model):
  title = models.TextField()
  organization = models.TextField()
  description = models.TextField()
  amount = models.IntegerField()
  deadline = models.DateField()
  education = models.TextField()
  state = models.TextField()
  ethnicity = models.TextField()
  women = models.BooleanField()
  lgbt = models.BooleanField()
  veteran = models.BooleanField()
  immigrant = models.BooleanField()
  url = models.URLField()
  image_url = models.URLField()

class User(models.Model):
  first_name = models.TextField()
  last_name = models.TextField()
  image_url = models.URLField()
  grants = models.ManyToManyField(Grant, blank=True)
  