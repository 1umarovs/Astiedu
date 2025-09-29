from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from apps.cauth.forms import AdmissionForm
from apps.cauth.models import Admission , User
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required
def admission_view(request):
    user = request.user
    current_year = timezone.now().year
    current_semester = 'winter' if timezone.now().month < 7 else 'summer'

    # Foydalanuvchining faol admissionini olish
    active_admission = Admission.objects.filter(user=user, active=True).first()

    if request.method == 'POST':
        form = AdmissionForm(request.POST, request.FILES, instance=active_admission)
        if form.is_valid():
            admission = form.save(commit=False)
            admission.user = user
            admission.semester = current_semester
            admission.year = current_year
            admission.active = True
            admission.save()
            messages.success(request, "Qabul qilish ma'lumotlari muvaffaqiyatli saqlandi!")
            return redirect('main:home')
        else:
            messages.error(request, "Formada xatolik bor, iltimos tekshiring!")
    else:
        form = AdmissionForm(instance=active_admission)

    context = {
        'form': form,
        'active_admission': active_admission
    }
    return render(request, 'profile/profile_edit.html', context)


@login_required
def admission_delete(request, pk):
    admission = get_object_or_404(Admission, pk=pk, user=request.user)
    admission.delete()
    messages.success(request, "Admission muvaffaqiyatli o‘chirildi!")
    return redirect('main:home')


@login_required
def admission_redirect(request,id):
    user = request.user
    current_year = timezone.now().year
    current_semester = 'winter' if timezone.now().month < 7 else 'summer'

    # Foydalanuvchining joriy semestr admissionini tekshirish
    admission = Admission.objects.filter(user=user, year=current_year, semester=current_semester , active=True).first()

    if admission:
        # Agar admission mavjud bo‘lsa, detail page ga yuborish
        return redirect('cauth:admission_detail', id=id)
    else:
        # Agar admission mavjud bo‘lmasa, create page ga yuborish
        return redirect('cauth:admission')



@login_required
def admission_detail(request, id):
    user = get_object_or_404(User, id=id)
    current_year = timezone.now().year
    current_semester = 'winter' if timezone.now().month < 7 else 'summer'

    admission = Admission.objects.filter(user=user, year=current_year, semester=current_semester , active=True).first()
    if not admission:
        # admission topilmasa create page ga yo'naltirish mumkin
        return redirect('cauth:admission')

    return render(request, 'admission_detail.html', {'admission': admission})