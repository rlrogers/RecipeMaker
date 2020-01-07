from django.db import models
from datetime import timezone

class RecipeDetails(models.Model):
    Dish = models.CharField(max_length=50, blank=True)
    # description = models.CharField(max_length=50, blank=True)
    number_of_ingredients = models.IntegerField(blank=True)
    # ingredient_amount = models.DecimalField( max_digits=2, decimal_places=2, null=True)
    # instruction = models.TextField("Place instruction here...", max_length=1000)
    # prep_time = models.IntegerField( blank=True)
    # cooking_time = models.IntegerField( default=0)
    # serves_amount = models.IntegerField(blank=True)
    # serves_ppl = models.IntegerField(blank=True)
    # published_date = models.DateTimeField(default=timezone.now)
    class Meta:
        verbose_name_plural = "Recipe Details"
    
