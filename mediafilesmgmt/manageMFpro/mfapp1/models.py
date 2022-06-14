from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_name = models.CharField(max_length=50)
    profile = models.CharField(max_length=50)
    salary = models.FloatField()
    email = models.EmailField()
    mblno = models.IntegerField()
    picture = models.ImageField(upload_to='pic')
    resume = models.FileField(upload_to='mediafile')
