from django.shortcuts import render
from apps.cauth.models import User
from apps.cauth.models import residential_address , GraduatedEducation
from django.contrib.auth import login , authenticate
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout
# Create your views here.
def login_view(request):
    user = request.POST.get('email')
    password = request.POST.get('password')
    if request.method == 'POST':
        user = authenticate(request, username=user, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:home')
        else:
            messages.error(request, 'Foydalanuvchi mavjud emas !')
            return redirect('cauth:login')
    return render(request, 'auth/login.html')

def registration_view(request):
    fullname = request.POST.get('fullname')
    email = request.POST.get('email')
    password = request.POST.get('password')
    password_confirmation = request.POST.get('password_confirmation')

    if request.method == 'POST':
        if all([fullname, email, password, password_confirmation]):
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Bu foydalanuvchi allaqachon mavjud !')
                return redirect('cauth:register')
            if password == password_confirmation:
                user = User.objects.create_user(fullname=fullname, email=email, password=password,username=email)
                residential_address.objects.create(user=user)
                GraduatedEducation.objects.create(user=user)

                authenticate(request, username=email, password=password)
                login(request, user)
                return redirect('main:home')
            else:
                messages.error(request, 'Parollar mos kelmaydi !')
                return redirect('cauth:register')
        else:
            messages.error(request, 'Barcha maydonlar to\'liq emas !')
            return redirect('cauth:register')    
    return render(request, 'auth/register.html')


def logout_view(request):
    logout(request)
    return redirect('main:home')