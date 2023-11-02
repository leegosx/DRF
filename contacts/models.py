from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    birthday = models.DateField()
        
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'