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

def dynamic_lookup_view(request, my_id):
    obj = RecipeDetails.objects.get(id=my_id)
    context = {
        "object": obj
    }
    return render(request, "recipe/detail.html")


# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             # now the data is good
#             print(my_form.cleaned_data)
#             RecipeDetails.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render(request, "recipe/product_create.html", context)


# def product_create_view(request):
#     my_new_title = request.POST.get('Dish')
#     print(my_new_title)
#     context = {}
#     return render(request, "recipe/product_create.html", context)

# Clean up or toss below
# def render_initial_data(request):
#     initial_data = {
#         'dish': "Initial Data"
#     }
#     obj = Product.objects.get(id=1)
#     form = RawProductForm(request.POST or None, initial=initial_data, instance=obj)
#     context = {
#         'form': form
#     }
#     return render(request, "recipe/product_create.html", context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "recipe/product_create.html", context)

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
