# pokedex/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pokemon_id>/', views.detail, name='detail'),
    path('', views.pokemon_list, name='pokemon_list'),
]
