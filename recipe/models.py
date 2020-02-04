from django.db import models
# cleanup timezone imports below
from django.utils import timezone
from django.contrib.auth.models import User

class RecipeDetails(models.Model):
    Dish = models.CharField(max_length=50, blank=False)
    ingredients = models.CharField( max_length=1000, blank=False, default="Separate ingredients with a comma")
    instruction = models.TextField(default="Place instruction here...", max_length=5000, blank=False)
    prep_time = models.IntegerField( blank=False, default=5)
    cooking_time = models.IntegerField( blank=False)
    servings = models.IntegerField(blank=True, default=1)
    published_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name_plural = "Recipe Details"
    
