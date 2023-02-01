from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    qty = models.IntegerField()


class Brand(models.Model):
    name = models.CharField("Brand Name", max_length=100)

    # def __str__(self):
    #     return self.name

    def __str__(self):
        return f"Name:{self.name}"
