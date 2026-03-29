from django.db import models
class Student(models.Model):   # base class
    name=models.CharField(max_length=100)
    age = models.IntegerField()
    reg_no =models.IntegerField()
    dept= models.CharField(max_length=50)
def __str__(self):
    return self.name
# Create your models here.
