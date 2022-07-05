from distutils.command import upload
from tkinter import N
from django.db import models

# Create your models here.

class CVmodel(models.Model):
    studentName=models.CharField(max_length=100,null=True)
    studentdob=models.DateField(null=False, blank=False)
    studentgender=models.CharField(max_length=100,null=False)
    studentcat=models.CharField(max_length=100,null=False)
    studentemail=models.EmailField(null=False, blank=False)
    studentpnumber=models.IntegerField(null=False, blank=False)
    studentaddress=models.CharField(max_length=200,null=False) 
    personalPhoto=models.ImageField(upload_to='imgfolder')
    signaturePhoto=models.ImageField(upload_to='imgfolder')
    
    def __str__(self):
        return self.studentName