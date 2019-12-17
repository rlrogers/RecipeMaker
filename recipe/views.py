from django.shortcuts import render
from django.http import HttpResponse
from .models import RecipeDetails


def index(request):
    return render(request, 'recipe/index.html')
