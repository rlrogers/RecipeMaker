from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class RecipeDetails(models.Model):
    Dish = models.CharField(max_length=50, blank=True)
    ingredients = models.CharField( max_length=1000, blank=False, default="Separate ingredients with a comma")
    instruction = models.TextField(default="Place instruction here...", max_length=5000, blank=False)
    prep_time = models.IntegerField( blank=False, default=5)
    cooking_time = models.IntegerField( blank=False)
    servings = models.IntegerField(blank=True, default=1)
    published_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  
    class Meta:
            verbose_name_plural = "Recipe Details"

    def get_absolute_url(self):
        return reverse("recipe:recipe-detail", kwargs={"id": self.id})

    def __str__(self):
        return self.Dish

    
    
