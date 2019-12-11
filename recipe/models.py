from django.db import models


class RecipeDetails(models.Model):
    # cook = models.ForeignKey("Cook.Model", verbose_name=_("cook"), on_delete=models.CASCADE) Will add Cook App later
    Dish_Author = models.CharField( max_length=50)
    Dish = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    number_of_ingredients = models.IntegerField(blank=True)
    ingredient_amount = models.DecimalField( max_digits=2, decimal_places=2)
    instruction = models.TextField(
        "Place instruction here...", max_length=1000)
    prep_time = models.IntegerField()
    cooking_time = models.IntegerField()
    serves_amount = models.IntegerField()
    serves_ppl = models.IntegerField()
    published_date = models.DateTimeField('Recipe made:')
    class Meta:
        verbose_name_plural = "RecipeDetails"
    def __str__(self):
        return self.name
    
