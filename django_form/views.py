from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm, RestaurantCreateForm


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


def student_create_form(request):
    form = StudentForm(request.POST or None)
    errors = None
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    else:
        form = StudentForm()

    context = {"form": form, "errors": errors}
    return render(request, 'django_form/row_form.html', context)


def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        location = request.POST.get('location')
        category = request.POST.get('category')
        RestaurantCreateForm.objects.create(
            name=name,
            location=location,
            category=category,
        )
    return render(request, 'django_form/row_form.html')


def restaurant_create(request):
    form = RestaurantCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        RestaurantCreateForm.objects.create(
            name=form.cleaned_data.get("name"),
            location=form.cleaned_data.get("location"),
            category=form.cleaned_data.get("category"),
        )
    if form.errors:
        errors = form.errors
    context = {"form": form, "errors": errors}
    return render(request, 'index.html', context)