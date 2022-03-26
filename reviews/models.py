from typing_extensions import Required
from django.db import models

# Create your models here.
class Resenas(models.Model):
    name=models.CharField('Name',max_length=50)
    email=models.EmailField('Email')
    star=models.IntegerField('Stars',null=True, blank=True)
    message=models.TextField('Message', max_length=500)
    image=models.ImageField('Image',null=True,blank=True)
    
    def __str__(self):
        return self.name + '-'+ self.email
