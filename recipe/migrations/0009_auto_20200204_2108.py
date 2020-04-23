# Generated by Django 3.0 on 2020-02-04 21:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe', '0008_auto_20200109_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipedetails',
            name='number_of_ingredients',
        ),
        migrations.AddField(
            model_name='recipedetails',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='recipedetails',
            name='ingredients',
            field=models.CharField(default='Separate ingredients with a comma', max_length=1000),
        ),
        migrations.AddField(
            model_name='recipedetails',
            name='instruction',
            field=models.CharField(default='Place instruction here...', max_length=5000),
        ),
        migrations.AddField(
            model_name='recipedetails',
            name='prep_time',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='recipedetails',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='recipedetails',
            name='servings',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='recipedetails',
            name='Dish',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='recipedetails',
            name='cooking_time',
            field=models.IntegerField(),
        ),
    ]