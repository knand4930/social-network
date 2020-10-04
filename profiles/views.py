from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile, RelationShip
from .forms import ProfileModelForm

# Create your views here.


# Create your views here.
def my_profile_view(request):
    profiles = Profile.objects.get(user=request.user)
    form = ProfileModelForm(request.POST or None, request.FILES or None, instance=profiles)
    confirm = False

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm = True

    context = {
        'profiles': profiles,
        'form':form,
        'confirm':confirm,
    }
    return render(request, 'profiles/myprofile.html', context)