from django.db import models
from apps.cauth.models import User

class residential_address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , related_name='residential_address')
    country = models.CharField(max_length=255 , null=True , blank=True)
    region = models.CharField(max_length=255 , null=True , blank=True)
    citizenship = models.CharField(max_length=255 , null=True , blank=True)
    address = models.CharField(max_length=255 , null=True , blank=True)
    index = models.CharField(max_length=255 , null=True , blank=True)

    def __str__(self):
        return self.user.fullname
    
    
class GraduatedEducation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , related_name='GraduatedEducation')
    country = models.CharField(max_length=255 , null=True , blank=True)
    region = models.CharField(max_length=255 , null=True , blank=True)
    institution = models.CharField(max_length=255 , null=True , blank=True)
    education_type = models.CharField(max_length=255 , null=True , blank=True)
    speciality = models.CharField(max_length=255 , null=True , blank=True)
    graduation_date = models.DateField( null=True , blank=True)
    diploma_number = models.CharField(max_length=255 , null=True , blank=True)
    
    def __str__(self):
        return self.user.fullname