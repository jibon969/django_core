from django.shortcuts import render
from .models import Student


def student_list(request):
    queryset = Student.objects.all()
    context = {
        "queryset": queryset,
    }
    return render(request, "curd/student-list.html", context)
