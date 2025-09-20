from django.shortcuts import render
from apps.core.models import Trips
from django.core.paginator import Paginator

def foreign_trips(request):
    trips = Trips.objects.defer('description', 'description_uz', 'description_en', 'description_ru').all()
    paginator = Paginator(trips, 3)
    page = request.GET.get('page')
    trips = paginator.get_page(page)
    context = {
        'trips': trips
    }
    return render(request, 'foreign-trips-and-visits.html', context)

def single_trips(request,id):
    trip = Trips.objects.get(id=id)
    others = Trips.objects.exclude(id=id).defer('description', 'description_uz', 'description_en', 'description_ru').all()
    return render(request, 'foreign-trips-and-visit/single/single.html', {'trip': trip, 'others': others})