from django.shortcuts import render, redirect
from .forms import UserRegistration
from django.contrib import messages


def registration(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} успешно зарегистрирован')
            return redirect('main_page')
    else:
        form = UserRegistration()
    return render(request, 'registration/registration.html', context={'form': form})