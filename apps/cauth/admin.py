from django.contrib import admin
from .models import User , residential_address , GraduatedEducation , Admission
# Register your models here.

admin.site.register(User)
admin.site.register(residential_address)
admin.site.register(GraduatedEducation)
admin.site.register(Admission)
