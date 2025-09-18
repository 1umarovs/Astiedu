from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    fullname = models.CharField(max_length=255)
    image = models.ImageField(upload_to='users', null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    passport_number = models.CharField(max_length=255, null=True, blank=True)
    brithday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=255, null=True, blank=True)

    # AbstractUser ichidagi emailni override qilib unique qilamiz
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"  # endi login va superuser yaratishda email ishlatiladi
    REQUIRED_FIELDS = ["fullname", "username"]  
    # "username" ni REQUIRED_FIELDS ga qo‘shish kerak, chunki AbstractUser uni ham majburiy qiladi

    def __str__(self):
        return self.fullname if self.fullname else self.email

