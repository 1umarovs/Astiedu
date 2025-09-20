from modeltranslation.translator import translator, TranslationOptions
from .models import InternationalExchangeProgram, AdvancedTraining , Trips, Partner_university

class InternationalExchangeProgramTranslationOptions(TranslationOptions):
    fields = ('university_name', 'country')

class AdvancedTrainingTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

class TripsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

class Partner_universityTranslationOptions(TranslationOptions):
    fields = ('university_name', 'country')

translator.register(InternationalExchangeProgram, InternationalExchangeProgramTranslationOptions)
translator.register(AdvancedTraining, AdvancedTrainingTranslationOptions)
translator.register(Trips, TripsTranslationOptions)
translator.register(Partner_university, Partner_universityTranslationOptions)