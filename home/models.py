from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image


def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    megabyte_limit = 5.0
    if filesize > megabyte_limit * 1024 * 1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))


class SliderImage(models.Model):
    image = models.ImageField(upload_to="a/b/c/", validators=[validate_image])
    height = models.PositiveIntegerField(editable=False, null=True)
    width = models.PositiveIntegerField(editable=False, null=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        # Calculate the height and width of the image before saving
        if self.image:
            with Image.open(self.image.path) as img:
                self.height = img.height
                self.width = img.width
        super().save(*args, **kwargs)
