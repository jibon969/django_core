from django.contrib import admin
from .models import Department, Student


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name"]


class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "dept", "roll"]

    class Meta:
        model = Student


admin.site.register(StudentAdmin, Student)