from django.shortcuts import render, redirect
from .forms import UserRegistration, UserUpdateForm, Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import DetailView


def registration(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} успешно зарегистрирован')
            return redirect('login')
    else:
        form = UserRegistration()
    return render(request, 'registration/registration.html', context={'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        update_profile = Profile(request.POST, request.FILES, instance=request.user.profile)
        update_user = UserUpdateForm(request.POST, instance=request.user)

        if update_profile.is_valid() and update_user.is_valid():
            update_profile.save()
            update_user.save()
            messages.success(request, f'Данные успешно обновлены')
            return redirect('profile')
    else:
        update_profile = Profile(instance=request.user.profile)
        update_user = UserUpdateForm(instance=request.user)

    data = {
        'update_profile': update_profile,
        'update_user': update_user,
    }

    return render(request, 'registration/profile.html', context=data)


class ProfileUser(DetailView):
    template_name = 'registration/profile_user.html'
    model = User
    context_object_name = 'user'
    slug_field = 'username'
    slug_url_kwarg = 'username'
