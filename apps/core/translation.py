from modeltranslation.translator import translator, TranslationOptions
from .models import InternationalExchangeProgram, AdvancedTraining , Trips, Partner_university , HonoraryProfessors , InternationalStudents , InternationalStudentsImages , Ranking

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



translator.register(InternationalExchangeProgram, InternationalExchangeProgramTranslationOptions)
translator.register(AdvancedTraining, AdvancedTrainingTranslationOptions)
translator.register(Trips, TripsTranslationOptions)
translator.register(Partner_university, Partner_universityTranslationOptions)
translator.register(HonoraryProfessors, HonoraryProfessorsTranslationOptions)
translator.register(InternationalStudents, InternationalStudentsTranslationOptions)
translator.register(Ranking, RankingTranslationOptions)