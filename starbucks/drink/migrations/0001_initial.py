# Generated by Django 3.0.7 on 2020-07-10 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'allergy',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drink.Category')),
            ],
            options={
                'db_table': 'drink',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'menu',
            },
        ),
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'nutrition',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.CharField(max_length=1000)),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drink.Drink')),
            ],
            options={
                'db_table': 'image',
            },
        ),
        migrations.CreateModel(
            name='Drink_Nutrition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drink.Drink')),
                ('nutrition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drink.Nutrition')),
            ],
            options={
                'db_table': 'drink_nutrition',
            },
        ),
        migrations.CreateModel(
            name='Drink_Allergy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drink.Allergy')),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drink.Drink')),
            ],
            options={
                'db_table': 'drink_allergy',
            },
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drink.Drink')),
            ],
            options={
                'db_table': 'detail',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drink.Menu'),
        ),
    ]
