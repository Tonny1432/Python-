from django.db import models
class students(models.Model):  #models.Model is the base class & students is the child class
     s_name = models.CharField(max_length=50)
     s_age = models.IntegerField()
     s_dept =models.CharField(max_length=50)
     s_reg = models.IntegerField()
     s_email= models.CharField(max_length=100)

"""class subject(models.Model):
     cs = models.IntegerField()
     emf =models.IntegerField()
     vlsi = models.IntegerField()
     trlf = models.IntegerField()
"""     
     
