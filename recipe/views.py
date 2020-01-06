from django.shortcuts import render
from django.http import HttpResponse
from .models import RecipeDetails


def home_view(self):
    return HttpResponse("<h1>Recipe Home Page</h1>")

def index(request):
    latest_recipes = RecipeDetails.objects.order_by('-pub_date')[:5]
    return render(request, 'recipe/index.html')

def test(request):
    return HttpResponse( "Here's the Test page response")


# def about(request):
#     return render(request, 'recipe/index.html')


