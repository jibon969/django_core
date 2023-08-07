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
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        password = request.POST.get('password')

        obj = RestaurantCreateForm.objects.create(
            name=name,
            email=email,
            phone=phone,
            address=address,
            password=password

        )
    return render(request, 'django_form/row_form.html')
