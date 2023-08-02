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


