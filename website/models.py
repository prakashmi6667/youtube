from django.db import models

# Create your models here.
class user(models.Manager):
    objects = models.Manager()

    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    profile = models.ImageField(upload_to="userProfile/")