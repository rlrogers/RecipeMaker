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
