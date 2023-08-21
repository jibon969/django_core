# https://blog.devgenius.io/how-to-create-an-abstract-model-class-in-django-e1e77048b3b7

from django.db import models


# class Car(models.Model):
#     brand = models.CharField(max_length=100)
#     doors = models.PositiveIntegerField()
#
#
# class Jet(models.Model):
#     brand = models.CharField(max_length=100)
#     wing_type = models.CharField(max_length=30)
#
#
# class Bike(models.Model):
#     brand = models.CharField(max_length=100)


class Common(models.Model):
    brand = models.CharField(max_length=100)

    class Meta:
        abstract = True


class Car(Common):
    doors = models.PositiveIntegerField()
    brand = models.CharField(max_length=30)


class Jet(Common):
    wing_type = models.CharField(max_length=30)


class Bike(Common):
    pass
