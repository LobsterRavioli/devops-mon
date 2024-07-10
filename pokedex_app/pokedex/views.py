from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

# pokedex/views.py

from django.shortcuts import render, get_object_or_404
from .models import Pokemon

def index(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'pokedex/index.html', {'pokemons': pokemons})

def detail(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    return render(request, 'pokedex/detail.html', {'pokemon': pokemon})

def pokemon_list(request):
    # Recupera tutti i Pokémon dal database
    pokemons = Pokemon.objects.all()

    # Passa i Pokémon al template per essere visualizzati
    context = {
        'pokemons': pokemons
    }
    return render(request, 'pokedex/pokemon_list.html', context)

