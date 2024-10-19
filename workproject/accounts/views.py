# accounts/views.py
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomLoginForm
from django.contrib.auth import login


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Сохраняем нового пользователя
            login(request, user)  # Автоматически логиним пользователя после регистрации
            return redirect('main')  # Перенаправление на главную страницу
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    form = CustomLoginForm()
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')  # Перенаправление на главную страницу после входа
    return render(request, 'accounts/login.html', {'form': form})
