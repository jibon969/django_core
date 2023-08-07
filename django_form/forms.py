from django import forms
from .models import Student, RestaurantLocation


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class RestaurantCreateForm(forms.Form):
    class Meta:
        model = RestaurantLocation
        fields = "__all__"

