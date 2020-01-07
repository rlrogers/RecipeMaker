from django.shortcuts import render
from django.http import HttpResponse
from .models import RecipeDetails


def home_view(request):
    return render(request, "home.html", {})

def index(request):
    latest_recipes = RecipeDetails.objects.order_by('-pub_date')[:5]
    return render(request, 'recipe/index.html')

def test(request):
    context = {
        "test_text": "Success The test context text and confirm test number of 123 =",
        "my_number": 123,
        "my_list": [123, 312, 789]
    }
    return render(request, "test.html", context)


# def about(request):
#     return render(request, 'recipe/index.html')


