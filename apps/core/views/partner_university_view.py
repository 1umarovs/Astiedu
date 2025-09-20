from django.shortcuts import render
from apps.core.models import Partner_university, InternationalExchangeProgram




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