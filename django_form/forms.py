from django import forms
from .models import Student, RestaurantLocation


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class RestaurantCreateForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    address = forms.CharField()
    password = forms.CharField()

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name ? ")
        return name

    def clean_email(self):
        name = self.cleaned_data.get("email")
        if name == ".edu":
            raise forms.ValidationError("We are not excpet .edu email ")
        return name

    def clean_address(self):
        name = self.cleaned_data.get("address")
        if name == "Dhaka":
            raise forms.ValidationError(" আপনি ভুল ঠিকানা দিয়েছেন ")
        return name