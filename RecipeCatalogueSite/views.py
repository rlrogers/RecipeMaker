from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

# def about(request):
#     return HttpResponse('HttpResponse, about.html')


def render_initial_data(request):
    initial_data = {
        "Dish": "My Awesome Dish"
    }
    form = Product(request.POST or NONE, initial=initial_data)
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)