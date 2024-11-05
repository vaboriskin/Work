from django.urls import path
from . import views

urlpatterns = [
    path('', views.vote_page, name ='vote_page'),
    path('edit_score/<int:score_id>/', views.edit_score, name='edit_score'),
    path('delete_score/<int:score_id>/', views.delete_score, name='delete_score'),

]
