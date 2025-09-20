from django.shortcuts import render
from apps.core.models import InternationalExchangeProgram

def home(request):
    return render(request, 'index.html')



