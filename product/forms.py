from django import forms
from .models import Brand, Product


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = [
            '__all__'
        ]