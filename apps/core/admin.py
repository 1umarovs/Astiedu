from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(InternationalExchangeProgram)
class InternationalExchangeProgramAdmin(admin.ModelAdmin):
    list_display = ('university_name', 'country', 'official_website', 'university_logo')
    list_filter = ('university_name', 'country')
    search_fields = ('university_name', 'country')
    list_per_page = 10


admin.site.register(AdvancedTraining)
admin.site.register(Trips)
admin.site.register(Partner_university)
admin.site.register(HonoraryProfessors)
admin.site.register(InternationalStudents)
admin.site.register(InternationalStudentsImages)
admin.site.register(Ranking)
admin.site.register(AboutUzbekistan)
admin.site.register(EducationalAreas)
admin.site.register(Brochures)
admin.site.register(News)
admin.site.register(Hostel)
admin.site.register(HostelImages)

