from django.db import models

# Create your models here.


class MetaInfo(models.Model):
    title = models.CharField(max_length=63)
    image = models.FileField(blank=True, null=True,upload_to="Meta_tag_image")
    focus_keyword = models.TextField()
    meta_description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']