from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class UserModel(models.Model):
    name = models.CharField(max_length=50)
    number=models.CharField(max_length=12)
    adress=models.CharField(max_length=50)