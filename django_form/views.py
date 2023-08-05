from django.shortcuts import render
from .models import Student
# Create your views here.


def add_student(request):
    if request.method == "POST":
        name = request.method.get('name')
        dept = request.method.get('dept')
        description = request.method.get('description')
        Student.objects.create(
            name=name,
            dept=dept,
            description=description
        )
    return render(request, "django_form/row_form.html")