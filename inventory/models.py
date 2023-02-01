from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    qty = models.IntegerField()


class Brand(models.Model):
    name = models.CharField(max_length=100)
