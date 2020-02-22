from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from products.models import branch

class User(AbstractUser):
    gender=models.CharField(max_length=6)
    birthdate=models.DateField(blank=True, null=True)
    address=models.CharField(max_length=150,default='')

    def __str__(self):
        return self.username
