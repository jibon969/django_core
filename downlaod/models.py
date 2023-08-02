from django.db import models


class Student(models.Model):
    title = models.CharField(max_length=120)
    dept = models.CharField(max_length=120)
    roll = models.CharField(max_length=120)

    def __str__(self):
        return self.title
