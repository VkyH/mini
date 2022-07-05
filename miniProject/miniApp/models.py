from email.policy import default
from django.db import models

# Create your models here.

class minimg(models.Model):
    fname=models.CharField(max_length=100)
    personalPhoto= models.ImageField(default='imagesfolder')
    
    def __str__(self):
        return self.fname