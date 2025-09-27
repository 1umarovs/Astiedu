from django.shortcuts import render
from apps.core.models import Partner_university, InternationalExchangeProgram , EducationalAreas , Brochures




def partner_university(request):
    partner_university = Partner_university.objects.all()
    context = {
        'PU': partner_university
    }
    return render(request, 'international-partner-universities.html', context)



def international_exchange_program(request):
    international_exchange_program = InternationalExchangeProgram.objects.all()
    context = {
        'IEP': international_exchange_program
    }
    return render(request, 'international-exchange-program.html', context)


def specialities(request):
    specialities = EducationalAreas.objects.all()
    context = {
        'EA': specialities
    }
    return render(request, 'admission/specialities.html', context)


def brochures(request):
    brochures = Brochures.objects.all()
    context = {
        'Brochures': brochures
    }
    return render(request, 'admission/brochures.html', context)
