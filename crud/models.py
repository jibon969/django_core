from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=120)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="dept")
    roll = models.PositiveIntegerField()

    def __str__(self):
        return self.name
