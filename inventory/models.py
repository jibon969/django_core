from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_length=5, decimal_places=2)
    data_added = models.DateTimeField(auto_now=True)
    data_updated = models.DateTimeField(auto_now=True)
    url = models.SlugField
    is_active = models.BooleanField()


class Brand(models.Model):
    name = models.CharField("Brand Name", max_length=100)

    # def __str__(self):
    #     return self.name

    def __str__(self):
        return f"Name:{self.name}"
