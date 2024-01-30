from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('ewa/', views.ewa, name='ewa'),
    path('conference/', views.conference, name='conf'),
    path('ewa/register/<str:random_id>/',
         views.ewa_delegate, name='ewa_delegate'),
    path('conference/register/<str:random_id>/',
         views.conference_delegate, name='conference_delegate'),
    path('profile/',
         views.past_events, name='past_events'),
]
