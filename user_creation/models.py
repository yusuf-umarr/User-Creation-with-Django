from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user_data(models.Model):
    first_name    = models.CharField(max_length=100)
    last_name     = models.CharField(max_length=100)
    username      = models.CharField(max_length=100)
    
