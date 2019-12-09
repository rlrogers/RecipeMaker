import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator


class Ingredients(models.Model):
    number_of_ingredients = models.IntegerField(blank=True, null=True, validators=[MaxValueValidator(25)])
    ingredient = models.CharField(max_length=20)
    ingredient_amount = models.IntegerField(blank=True, )
    published_date = models.DateTimeField('Recipe made:')

    
