from django.shortcuts import render
from apps.core.models import InternationalExchangeProgram , HonoraryProfessors

def home(request):
    return render(request, 'index.html')


def honorary_professors(request):
    honorary_professors = HonoraryProfessors.objects.all()
    return render(request, 'international-honorary-professors.html', {'HP': honorary_professors})
