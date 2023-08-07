from django.db import models
from .validators import validate_category


class Student(models.Model):
    name = models.CharField(max_length=120)
    dept = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.name


class RestaurantLocation(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, null=True, blank=True)
    category = models.CharField(max_length=120, null=True, blank=True, validators=[validate_category])
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
