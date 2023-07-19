from django.shortcuts import render, redirect
from .forms import UserRegistration
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
    return render(request, 'registration/profile.html')
