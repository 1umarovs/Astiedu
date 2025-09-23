from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.cauth.models import User , residential_address , GraduatedEducation


@login_required
def profile(request):
    user = User.objects.select_related('residential_address', 'GraduatedEducation').get(
        id=request.user.id
    )
    context = {
        'user': user,
        'address': getattr(user, 'residential_address', None),
        'education': getattr(user, 'GraduatedEducation', None),
    }
    return render(request, 'profile/profile.html', context)
