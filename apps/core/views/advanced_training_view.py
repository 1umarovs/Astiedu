from django.shortcuts import render
from apps.core.models import AdvancedTraining , AboutUzbekistan

def advanced_training(request):
    advanced_training = AdvancedTraining.objects.last()
    
    context = {
        'advanced_training': advanced_training
    }
    return render(request, 'international-development-education.html', context)

def about_uzbekistan(request):
    about_uzbekistan = AboutUzbekistan.objects.all()
    
    context = {
        'AU': about_uzbekistan
    }
    return render(request, 'admission/uzbekistan.html', context)