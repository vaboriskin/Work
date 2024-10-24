# accounts/urls.py
from django.urls import path
from .views import signup_view, login_view  # Импортируем представления

urlpatterns = [
    path('signup/', signup_view, name='signup'),  # URL для регистрации
    path('login/', login_view, name='login'),      # URL для входа
]
