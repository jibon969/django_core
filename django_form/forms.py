from django import forms
from .models import Student, RestaurantLocation


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class RestaurantCreateForm(forms.Form):
    name = forms.CharField()
    location = forms.EmailField()
    category = forms.CharField()

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name ? ")
        return name

    def clean_location(self):
        location = self.cleaned_data.get("address")
        if location == "Dhaka":
            raise forms.ValidationError(" আপনি ভুল ঠিকানা দিয়েছেন ")
        return location
