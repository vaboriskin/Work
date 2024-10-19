
from django.urls import path
from . import views

urlpatterns = [
    path('', views.participants_with_scores, name='scoretable'),
]