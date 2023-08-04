from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=120)
    dept = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.name
