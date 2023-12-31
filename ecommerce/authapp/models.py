from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)
    user_id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.username
