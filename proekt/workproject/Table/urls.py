
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_participants_scores, name='participant_scores'),
    path('get_all_scores/', views.get_all_scores, name='get_all_scores'),

]