from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.cauth.models import User, residential_address, GraduatedEducation
from apps.cauth.forms import UserForm, AddressForm, EducationForm


@login_required
def edit_profile_section(request, model, form_class, template="profile/profile_edit.html", related_name=None):
    """
    Umumiy update view (User, Address, Education uchun).
    """
    if model is User:
        instance = get_object_or_404(User, id=request.user.id)
    else:
        # Agar bog'liq obyekt bo'lmasa -> yaratib qo'yamiz (DoesNotExist xatosidan qutulish uchun)
        instance, _ = model.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = form_class(request.POST, request.FILES or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect("main:profile")
    else:
        form = form_class(instance=instance)

    return render(request, template, {"form": form})


@login_required
def user_edit(request):
    return edit_profile_section(request, User, UserForm)


@login_required
def address_edit(request):
    return edit_profile_section(request, residential_address, AddressForm)


@login_required
def education_edit(request):
    return edit_profile_section(request, GraduatedEducation, EducationForm)
