from django.db import models
from apps.cauth.models import User

class residential_address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    citizenship = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    index = models.CharField(max_length=255)
    
    
class GraduatedEducation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    education_type = models.CharField(max_length=255)
    speciality = models.CharField(max_length=255)
    graduation_date = models.DateField()
    diploma_number = models.CharField(max_length=255)
    
    