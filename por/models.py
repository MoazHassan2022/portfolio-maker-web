from django.contrib.auth.models import AbstractUser
from django.db import models

class Work(models.Model):
    username = models.CharField(max_length=64, default="", blank=True)
    title = models.CharField(max_length=64, default="", blank=True)
    description = models.CharField(max_length=300, default="", blank=True)
    webLink = models.CharField(max_length=64, default="", blank=True)
    imageLink = models.CharField(max_length=150, default="", blank=True)
    imageOnHoverLink = models.CharField(max_length=150, default="", blank=True)

class User(AbstractUser):
    worksList = models.ManyToManyField(Work, blank=True, related_name="users")
    facebook = models.CharField(max_length=64, default="", blank=True)
    whats = models.CharField(max_length=64, default="", blank=True)
    FirstName = models.CharField(max_length=64, default="", blank=True)
    LastName = models.CharField(max_length=64, default="", blank=True)
    description = models.CharField(max_length=300, default="", blank=True)
