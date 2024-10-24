
from django.urls import path
from . import views

urlpatterns = [
    path('', views.participant_scores, name='participant_scores'),
    path('get_scores/<int:participant_id>/', views.get_scores, name='get_scores'),

]