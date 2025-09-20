from django.shortcuts import render
from apps.core.models import AdvancedTraining

def advanced_training(request):
    advanced_training = AdvancedTraining.objects.last()
    context = {
        'advanced_training': advanced_training
    }
    return render(request, 'international-development-education.html', context)