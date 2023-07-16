import re
from django import forms
from django.forms import Textarea
from .models import Contact


EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'subject',
            'name',
            'phone',
            'email',
            'message',
        ]
    
        # Override the Customer some fields
        widgets = {
            'message': Textarea(attrs={'rows': 3, 'cols': 3}),
        }

    # Validation
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "hi":
            raise forms.ValidationError("Please provide valid name")
        if name == 1:
            raise forms.ValidationError("Please provide valid name")
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and not re.match(EMAIL_REGEX, email):
            raise forms.ValidationError('Invalid email format')
        if email == '.edu':
            raise forms.ValidationError(".edu email not allowed")
        return email

