from django import forms
from .models import Brand, Product


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = [
            '__all__'
        ]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            '__all__'
        ]

