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
    path('international-honorary-professors/', views.honorary_professors, name='honorary_professors'),
    path('international-students/', views.international_students, name='international_students'),
    path('international-ranking/', views.rankings, name='international_ranking'),
    path('cabinet/', views.profile, name='profile'),
    path('ranking/single/<int:id>/', views.single_ranking, name='ranking_single'),
    path('about-uzbekistan/', views.about_uzbekistan, name='about_uzbekistan'),
    path('admission/specialities/', views.specialities, name='specialities'),
    path('admission/brochures/', views.brochures, name='brochures'),
    path('all-news/', views.all_news, name='all_news'),
    path('all-news/single/<int:id>/', views.single_news, name='news_single'),
    path('admission/hostel-for-foreign-students/', views.hostel_for_foreign_students, name='hostel_for_foreign_students'),
    path('admission/hostel-for-foreign-students/single/<int:id>/', views.single_hostel, name='hostel_for_foreign_students_single'),
]