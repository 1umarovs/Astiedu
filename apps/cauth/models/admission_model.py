from django.db import models
from django.conf import settings
from django.utils import timezone

class Admission(models.Model):
    SEMESTER_CHOICES = (
        ('winter', 'Qish'),
        ('summer', 'Yoz'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='admissions')
    semester = models.CharField(max_length=10, choices=SEMESTER_CHOICES)
    year = models.PositiveIntegerField(default=timezone.now().year)
    
    # Files
    certificate_of_general_secondary_education = models.FileField(upload_to='admissions/certificate/')
    medical_file = models.FileField(upload_to='admissions/medical/')
    passport = models.FileField(upload_to='admissions/passports/')
    visa = models.FileField(upload_to='admissions/visa/')
    photo = models.ImageField(upload_to='admissions/photos/')

    active = models.BooleanField(default=True)  # active = current semester admission

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'semester', 'year')  # bir foydalanuvchi bir semestrda faqat 1 admission
        ordering = ['-year', '-semester']

    def save(self, *args, **kwargs):
        # agar yangi admission active bo‘lsa, eski semestr admission passive qilinadi
        if self.active:
            Admission.objects.filter(user=self.user, active=True).exclude(pk=self.pk).update(active=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.fullname} - {self.semester} {self.year}"
