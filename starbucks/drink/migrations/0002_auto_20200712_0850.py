# Generated by Django 3.0.7 on 2020-07-12 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drink', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nutrition',
            name='name',
        ),
        migrations.AddField(
            model_name='drink',
            name='en_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='nutrition',
            name='caffeine_mg',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='nutrition',
            name='one_serving_kcal',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='nutrition',
            name='protein_g',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='nutrition',
            name='saturated_fat_g',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='nutrition',
            name='sodium_mg',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='nutrition',
            name='sugars_g',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.DeleteModel(
            name='Drink_Nutrition',
        ),
    ]
