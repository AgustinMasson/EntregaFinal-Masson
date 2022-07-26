from django.db import models

# Create your models here.
class User(models.Model):

    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50, default="password2")
    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    team = models.CharField(max_length=50)