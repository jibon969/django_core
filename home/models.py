from django.db import models


class SliderImage(models.Model):
    image = models.FileField()

    def __str__(self):
        return str(self.id)