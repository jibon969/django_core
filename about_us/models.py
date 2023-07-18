from django.db import models
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField


class AboutInfo(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True, db_index=True)
    description = RichTextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']


class ReturnPolicy(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True, db_index=True)
    description = RichTextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']


class SecurityPrivacy(models.Model):
    title = models.CharField(max_length=110, blank=True, null=True, db_index=True)
    description = RichTextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']


class TermsConditions(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']


class MoneyRefund(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, db_index=True)
    description = RichTextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']


class DeliveryPayment(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, db_index=True)
    description = RichTextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']


# Create table for youtube video link
class YoutubeVideo(models.Model):
    title = models.CharField(max_length=120, db_index=True)
    video = EmbedVideoField(help_text="Copy youtube videos urls")  # same like models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']


class HelpCenter(models.Model):
    title = models.CharField(max_length=120, db_index=True)
    description = RichTextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']
