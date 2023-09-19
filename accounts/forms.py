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


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
