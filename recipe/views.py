from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from .models import RecipeDetails
# from .forms import ProductForm, RawProductForm`
from .forms import NewRecipeForm
# List View commented out below and imported random instead
# from django.views.generic import (
#     CreateView,
#     DetailView,
#     ListView,
#     UpdateView,
#     DeleteView,
# )

from django.views import generic


def home_view(request):
    context = {
        'recipe': RecipeDetails.objects.all()
    }
    return render(request, "home.html", context)

# class IndexView(generic.ListView):
#     template_name = "home.html"

#     def get_queryset(self):
#         return RecipeDetails.objects.all()

class RecipeCreatetView(generic.CreateView): 
    template_name = 'recipe/recipe_create.html'
    form_class = NewRecipeForm
    query_set = RecipeDetails.objects.all()
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class RecipeListView(generic.ListView): 
    query_set = RecipeDetails.objects.all() #recipe/<modelname>_list.html
    model = RecipeDetails
    template_name = 'recipe/recipe_list.html'
    context_object_name = 'recipes'
    # ordering = ['-date_posted']


# Work on this Detail view below 
class RecipeDetailView(generic.DetailView):
    template_name = 'recipe/recipe_detail.html'
    query_set = RecipeDetails.objects.all()
    model = RecipeDetails

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(RecipeDetails, id=id_)



def index(request):
    latest_recipes = RecipeDetails.objects.order_by('-pub_date')[:5]
    return render(request, 'recipe/index.html')



#  Commented below app for references as moving on to class-based
def product_create_view(request):
    form = NewRecipeForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "recipe/recipe_create.html", context)
