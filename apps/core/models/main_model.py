from django.db import models
from ckeditor.fields import RichTextField

class InternationalExchangeProgram(models.Model):
    university_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    official_website = models.URLField()
    university_logo = models.ImageField(upload_to='university_logo/')

    def __str__(self):
        return self.university_name

    class Meta:
        verbose_name = 'International Exchange Program'
        verbose_name_plural = 'International Exchange Programs'


class AdvancedTraining(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Advanced Training'
        verbose_name_plural = 'Advanced Trainings'

class Trips(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='trips/')
    description = RichTextField()
    date = models.DateField()

    class Meta:
        verbose_name = 'Trip'
        verbose_name_plural = 'Trips'    
    
    def __str__(self):
        return self.title



class Partner_university(models.Model):
    university_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    official_website = models.URLField()
    university_logo = models.ImageField(upload_to='partner_university_logo/')

    def __str__(self):
        return self.university_name

    class Meta:
        verbose_name = 'Partner University'
        verbose_name_plural = 'Partner Universities'



class HonoraryProfessors(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    description = RichTextField()
    img = models.ImageField(upload_to='honorary_professors/')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Honorary Professor'
        verbose_name_plural = 'Honorary Professors'
    