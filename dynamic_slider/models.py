from django.db import models


# Slider Models 10:32 AM 3/4/2020
class Slider(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True, help_text='slider title is mandatory')
    extraLargeDevices = models.ImageField(upload_to='slider/', null=True, blank=True, help_text="1920x597")
    largeDevices = models.ImageField(upload_to='slider/', null=True, blank=True, help_text="1400x400")
    mediumDevices = models.ImageField(upload_to='slider/', null=True, blank=True, help_text="800X400")
    smallDevices = models.ImageField(upload_to='slider/', null=True, blank=True, help_text="600x400")
    url_field = models.URLField(max_length=120, null=True, blank=True)
    value = models.IntegerField(null=True, blank=True, verbose_name="Slider Position")
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class SingleSlider(models.Model):
    title = models.CharField(max_length=120)
    about = models.CharField(max_length=150, blank=True, null=True)
    image = models.ImageField(help_text="width: 1600px & height: 575px")
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']
