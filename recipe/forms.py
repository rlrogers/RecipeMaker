from django import forms 
from .models import RecipeDetails



# Creating new form for testing 
class NewRecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeDetails
        fields = [
            'Dish',
            'cooking_time',
            'published_date'
        ]




# class ProductForm(forms.ModelForm):
#     Dish = forms.CharField(label='',
#             widget=forms.TextInput(attrs={"placeholder": "Name of Dish"}))
#     # email = forms.EmailField()
#     number_of_ingredients = forms.IntegerField(
#         required=False,
#         widget=forms.Textarea(
#             attrs={
#                 "placeholder":"Number of indgredients...",
#                 "class": "new-class-name two",
#                 "id": "my-id-for-textarea",
#                 "rows": 1,
#                 "cols": 12
#             })
#             )
#     class Meta:
#         model = RecipeDetails
#         fields = [
#             'Dish',
#             'number_of_ingredients',
#             'cooking_time'
#         ]

    # This below needs some cleaning, validation errors aren't being raised
    def clean_dish_title(self, *args, **kwargs):
        dish = self.clean_data.get("Dish")
        if "CFE" in dish:
            return dish
        else:
            raise forms.ValidationError("This is not a valid Title")
        return dish
        
    #  This works for reference, so work above according
    def clean_email(self, *arbs, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email")
        return email

# class RawProductForm(forms.Form):
#     Dish = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "your title"}))
#     number_of_ingredients = forms.CharField(
#         required=False,
#         widget=forms.Textarea(
#             attrs={
#                 "placeholder":"your description",
#                 "class": "new-class-name two",
#                 "id": "my-id-for-textarea",
#                 "rows": 20,
#                 "cols": 120
#             }))
#     cooking_time = forms.CharField(initial=199.99)