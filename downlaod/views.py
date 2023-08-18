from django.http import HttpResponse
import csv
from django.http import StreamingHttpResponse
from django.utils.encoding import smart_str
from .models import Student


# Students name
NAME = ['Jibon', 'Tamim', 'Sakib']
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


def download_model_field_csv(request):
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


def generate_csv_rows(queryset):
    """
    Generator function that yields rows for the CSV file.
    This function should be efficient and not load the entire data into memory.
    """
    yield ['title', 'dept', 'roll']  # Header row
    for item in queryset.values('title', 'dept', 'roll'):
        yield [item['title'], item['dept'], item['roll']]


def download_large_csv(request):
    # Fetch the data from the Student model
    queryset = Student.objects.all()
    # Prepare response and CSV writer
    response = StreamingHttpResponse(
        (smart_str(",").join(row) + "\n" for row in generate_csv_rows(queryset)), content_type='text/csv')

    # Set the filename for the downloaded CSV file
    response['Content-Disposition'] = 'attachment; filename="large_data.csv"'
    return response
