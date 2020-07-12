from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "menu"


class Category(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "category"


class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=10, decimal_places=2)
    sodium_mg = models.DecimalField(max_digits=10, decimal_places=2)
    saturated_fat_g = models.DecimalField(max_digits=10, decimal_places=2)
    sugars_g = models.DecimalField(max_digits=10, decimal_places=2)
    protein_g = models.DecimalField(max_digits=10, decimal_places=2)
    caffeine_mg = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "nutrition"


class Drink(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    nutrition = models.ForeignKey(Nutrition, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    en_name = models.CharField(max_length=100)

    class Meta:
        db_table = "drink"


class Image(models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    img_url = models.CharField(max_length=1000)

    class Meta:
        db_table = "image"


class Detail(models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)

    class Meta:
        db_table = "detail"


class Allergy(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "allergy"


class Drink_Allergy(models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    allergy = models.ForeignKey(Allergy, on_delete=models.CASCADE)

    class Meta:
        db_table = "drink_allergy"
