from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
    path('title/', views.title, name='title'),
    path('policy/', views.policy, name='policy'),
    path('terms/', views.terms, name='terms'),
]