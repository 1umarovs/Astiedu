from modeltranslation.translator import translator, TranslationOptions
from .models import *

class InternationalExchangeProgramTranslationOptions(TranslationOptions):
    fields = ('university_name', 'country')

class AdvancedTrainingTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

class TripsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

class Partner_universityTranslationOptions(TranslationOptions):
    fields = ('university_name', 'country')

class HonoraryProfessorsTranslationOptions(TranslationOptions):
    fields = ('name', 'country', 'description')

class InternationalStudentsTranslationOptions(TranslationOptions):
    fields = ('name', 'country', 'course', 'direction')

class RankingTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

class AboutUzbekistanTranslationOptions(TranslationOptions):
    fields = ('title',)

class EducationalAreasTranslationOptions(TranslationOptions):
    fields = ('title', 'e_type', 'e_form', 'e_language')


class BrochuresTranslationOptions(TranslationOptions):
    fields = ('title', 'language' , 'file')


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

class HostelTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(InternationalExchangeProgram, InternationalExchangeProgramTranslationOptions)
translator.register(AdvancedTraining, AdvancedTrainingTranslationOptions)
translator.register(Trips, TripsTranslationOptions)
translator.register(Partner_university, Partner_universityTranslationOptions)
translator.register(HonoraryProfessors, HonoraryProfessorsTranslationOptions)
translator.register(InternationalStudents, InternationalStudentsTranslationOptions)
translator.register(Ranking, RankingTranslationOptions)
translator.register(AboutUzbekistan, AboutUzbekistanTranslationOptions)
translator.register(EducationalAreas, EducationalAreasTranslationOptions)
translator.register(Brochures, BrochuresTranslationOptions)
translator.register(News, NewsTranslationOptions)
translator.register(Hostel, HostelTranslationOptions)