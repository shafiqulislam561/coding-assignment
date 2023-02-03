from django.db import models

# Create your models here.

class Parent(models.Model):

    id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    street=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip=models.CharField(max_length=100)
    
    def __str__(self):
        return self.first_name or ''

class Child(models.Model):
    
    id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    parent = models.ForeignKey('Parent', related_name='children', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.first_name or ''
