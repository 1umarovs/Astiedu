from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required


@login_required
def reset_password_view(request):
    old = request.POST.get('old_password')
    new = request.POST.get('password')
    new2 = request.POST.get('password_confirmation')

    if request.method == 'POST':
        if old == new:
            messages.error(request, 'Yangi parol eski parol bilan bir xil bo`lishi mumkin emas!')
            return redirect('cauth:reset-password')
    
        if new != new2:
            messages.error(request, 'Yangi parol va parolni tasdiqlash bir xil emas!')
            return redirect('cauth:reset-password')
        
        if not request.user.check_password(old):
            messages.error(request, 'Eski parol xato!')
            return redirect('cauth:reset-password')
        
        if new == new2:
            request.user.set_password(new)
            request.user.save()
            login(request, request.user)
            messages.success(request, 'Parol muvaffaqiyatli almashtirildi!')
            return redirect('main:home')
    
    return render(request, 'auth/reset.html')
