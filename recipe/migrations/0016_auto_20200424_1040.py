# Generated by Django 3.0 on 2020-04-24 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0015_auto_20200222_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipedetails',
            name='Dish',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
