from django import forms
from .models import User


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_login',
            'contact_number',
            'gender',
            'email',
        ]
