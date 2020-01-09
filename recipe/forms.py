from django import forms 
from .models import RecipeDetails

class ProductForm(forms.ModelForm):
    class Meta:
        model = RecipeDetails
        fields = [
            'Dish',
            'number_of_ingredients',
            'cooking_time'
        ] 

class RawProductForm(forms.Form):
    Dish = forms.CharField()
    number_of_ingredients = forms.CharField()
    cooking_time = forms.CharField()