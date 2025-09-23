from django.urls import path
from .views import login_view, registration_view, logout_view, reset_password_view , user_edit , address_edit , education_edit

app_name = 'cauth'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('reset-password/', reset_password_view, name='reset-password'),
    path('general-information-change/', user_edit, name='user-edit'),
    path('address-edit/', address_edit, name='address-edit'),
    path('graduated-education-edit/', education_edit, name='education-edit'),
]
