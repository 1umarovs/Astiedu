from django.contrib import admin
from .models import User , residential_address , GraduatedEducation
# Register your models here.

admin.site.register(User)
admin.site.register(residential_address)
admin.site.register(GraduatedEducation)
