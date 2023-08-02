from django.http import HttpResponse
import csv
from .models import Student

# Students name
NAME = ['Jibon', 'Payel', 'Sakib']
# QUIZ Subject
SUBJECT = ['Math', 'Programming', 'Database', 'Problem-Solving']


def download_csv(request):
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=student.csv'
    writer = csv.writer(response)
    writer.writerow(['id', 'Student Name', 'Dept', 'Roll'])
    for (name, sub) in zip(NAME, SUBJECT):
        writer.writerow([name, sub])
    return response


def downlaod_model_field_csv(request):
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="student.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow(['id', 'Student Name', 'Dept', 'Roll'])
    queryset = Student.objects.all()
    for q in queryset:
        writer.writerow([q.title, q.name, q.dept])
    return response


def csv_database_write(request):
    # Get all data from student Database Table
    student = Student.objects.all()

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="csv_database_write.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Name', 'Dept', 'Roll'])

    for s in student:
        writer.writerow([s.id, s.title, s.dept, s.roll])

    return response
