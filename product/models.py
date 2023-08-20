from django.db import models


class Brand(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True)
    image = models.FileField(blank=True, null=True)
    discount = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Product(models.Model):
    title = models.CharField(max_length=500)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=450)
    old_price = models.DecimalField(default=1000, max_digits=20, decimal_places=2)
    app_price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0)
    weight = models.CharField(max_length=20, help_text='20ml/20gm', null=True, blank=True)
    size = models.CharField(max_length=10, help_text='S/M/L/XL/32/34/36', null=True, blank=True)
    buy_one_get_one = models.BooleanField(default=False, blank=True)
    limit_buy = models.BooleanField(default=False, blank=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['timestamp']

