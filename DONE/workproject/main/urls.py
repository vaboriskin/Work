from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name ='main'),
    path('participants/', views.participant_list, name='participant_list'),
    path('participants/create/', views.participant_create, name='participant_create'),
    path('participants/<int:pk>/edit/', views.participant_edit, name='participant_edit'),
    path('participants/<int:pk>/delete/', views.participant_delete, name='participant_delete'),
    path('delete_all_participants/', views.delete_all_participants, name='delete_all_participants'),


]
