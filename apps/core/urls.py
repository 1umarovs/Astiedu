from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('international-exchange-program/', views.international_exchange_program, name='international_exchange_program'),
    path('foreign-trips-and-visits/', views.foreign_trips, name='foreign_trips'),
    path('international-development-education/', views.advanced_training, name='international_development_education'),
    path('foreign-trips-and-visits/single/<int:id>/', views.single_trips, name='foreign_trips_single'),
    path('international-partner-universities/', views.partner_university, name='partner_university'),
]