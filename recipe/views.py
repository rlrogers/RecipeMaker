from django.shortcuts import render
from django.http import HttpResponse
from .models import RecipeDetails
from .forms import ProductForm, RawProductForm

def home_view(request):
    return render(request, "home.html", {})

def index(request):
    latest_recipes = RecipeDetails.objects.order_by('-pub_date')[:5]
    return render(request, 'recipe/index.html')

def test(request):
    context = {
        "test_text": "Success The test context text and confirm test number of 123 = ",
        "test_number": 123
    }
    return render(request, "test.html", context)


def product_create_view(request):
    my_form = RawProductForm()
    context = {
        "form": my_form
    }
    return render(request, "recipe/product_create.html", context)


# def product_create_view(request):
#     my_new_title = request.POST.get('Dish')
#     print(my_new_title)
#     context = {}
#     return render(request, "recipe/product_create.html", context)

# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     context = {
#         'form': form
#     }
#     return render(request, "recipe/product_create.html", context)

def product_detail_view(request):
    obj = RecipeDetails.objects.get(id=1)
    # context = {
    #     'Dish': obj.Dish,
    #     'num': obj.number_of_ingredients
    # }
    context = {
        'object': obj
    }
    return render(request, "recipe/detail.html", context)

# def about(request):
#     return render(request, 'recipe/index.html')
