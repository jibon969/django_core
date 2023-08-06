from django.shortcuts import render
from .models import Student
from .forms import StudentForm


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


def add_student_form(request):
    form = StudentForm(request.POST or None)
    errors = None
    if form.is_valid():
        Student.objects.create(
            name=form.cleaned_data.get("name"),
            dept=form.cleaned_data.get("dept"),
            description=form.cleaned_data.get("description"),
        )
    if form.errors:
        errors = form.errors
    context = {"form": form, "errors": errors}
    return render(request, 'django_form/row_form.html', context)
