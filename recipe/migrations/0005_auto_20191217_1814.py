# Generated by Django 3.0 on 2019-12-17 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_auto_20191217_1714'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipedetails',
            options={'verbose_name_plural': 'Recipe Details'},
        ),
        migrations.AddField(
            model_name='recipedetails',
            name='Dish',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='recipedetails',
            name='cooking_time',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='recipedetails',
            name='description',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='recipedetails',
            name='ingredient_amount',
            field=models.DecimalField(decimal_places=2, max_digits=2, null=True),
        ),
        migrations.AddField(
            model_name='recipedetails',
            name='instruction',
            field=models.TextField(default='instructions', max_length=1000, verbose_name='Place instruction here...'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipedetails',
            name='number_of_ingredients',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipedetails',
            name='prep_time',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipedetails',
            name='serves_amount',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipedetails',
            name='serves_ppl',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
